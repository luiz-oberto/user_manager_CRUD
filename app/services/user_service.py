from app.database import get_connection
from werkzeug.security import generate_password_hash

def create_user(user):
    conn = get_connection()
    cur = conn.cursor()

    senha_hash = generate_password_hash(user.senha)

    query = """
        INSERT INTO usuario (nome, email, senha_hash, is_superuser)
        VALUES (%s, %s, %s, %s)
        RETURNING id_usuario, nome, email, is_superuser
    """

    cur.execute(query, (
        user.nome,
        user.email,
        senha_hash,
        user.is_superuser
    ))

    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return result


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
