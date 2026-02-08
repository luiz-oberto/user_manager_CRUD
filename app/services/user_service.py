from app.database import get_connection
from psycopg2.errors import UniqueViolation
from fastapi import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash

# create de usuário com tratamento de email duplicado
def create_user(user):
    conn = get_connection()
    cur = conn.cursor()

    senha_hash = generate_password_hash(user.senha)
    email = user.email.lower().strip()

    try:
        cur.execute(
            """
            INSERT INTO usuario (nome, email, senha_hash, is_superuser)
            VALUES (%s, %s, %s, %s)
            RETURNING id_usuario, nome, email, is_superuser
            """,
            (user.nome, email, senha_hash, user.is_superuser)
        )

        result = cur.fetchone()
        conn.commit()
        return result

    except UniqueViolation:
        conn.rollback()
        raise HTTPException(
            status_code=409,
            detail="Email já cadastrado"
        )

    finally:
        cur.close()
        conn.close()


def list_users():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id_usuario, nome, email, is_superuser
        FROM usuario
    """)

    users = cur.fetchall()
    cur.close()
    conn.close()

    return users


def get_user_by_id(user_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id_usuario, nome, email, is_superuser
        FROM usuario
        WHERE id_usuario = %s
        """,
        (user_id,)
    )

    user = cur.fetchone()
    cur.close()
    conn.close()

    return user

# update de usuário com tratamente de emails duplicados
def update_user(user_id: int, user):
    conn = get_connection()
    cur = conn.cursor()

    email = user.email.lower().strip() if user.email else None

    try:
        query = """
            UPDATE usuario
            SET nome = COALESCE(%s, nome),
                email = COALESCE(%s, email),
                is_superuser = COALESCE(%s, is_superuser)
            WHERE id_usuario = %s
            RETURNING id_usuario, nome, email, is_superuser
        """

        cur.execute(query, (
            user.nome,
            email,
            user.is_superuser,
            user_id
        ))

        updated_user = cur.fetchone()
        conn.commit()

        return updated_user

    except UniqueViolation:
        conn.rollback()
        raise HTTPException(
            status_code=409,
            detail="Email já cadastrado por outro usuário"
        )

    finally:
        cur.close()
        conn.close()


def delete_user(user_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        DELETE FROM usuario
        WHERE id_usuario = %s
        RETURNING id_usuario
        """,
        (user_id,)
    )

    deleted = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return deleted


def authenticate_user(email: str, senha: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id_usuario, nome, email, senha_hash, is_superuser
        FROM usuario
        WHERE email = %s
        """,
        (email.lower().strip(),)
    )

    user = cur.fetchone()
    cur.close()
    conn.close()

    if not user: # se usuário inexistente
        return None

    if not check_password_hash(user["senha_hash"], senha): # se senha não bateu
        return None

    # remove senha_hash antes de retornar
    return {
        "id_usuario": user["id_usuario"],
        "nome": user["nome"],
        "email": user["email"],
        "is_superuser": user["is_superuser"]
    }