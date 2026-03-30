from app.database import get_connection
from werkzeug.security import generate_password_hash

import os

def create_initial_admin():
    conn = get_connection()
    cur = conn.cursor()

    admin_email = os.getenv("ADMIN_EMAIL", "admin@local")
    admin_password = os.getenv("ADMIN_PASSWORD", "Admin@123")

    # Verifica se já existe superuser
    cur.execute("SELECT * FROM usuario WHERE is_superuser = TRUE LIMIT 1;")
    existing_admin = cur.fetchone()

    if existing_admin:
        print("✔️ Superusuário já existe")
        cur.close()
        conn.close()
        return

    # Cria hash
    hashed_password = generate_password_hash(admin_password)

    # Cria usuário admin
    cur.execute("""
        INSERT INTO usuario (nome, email, senha_hash, is_superuser)
        VALUES (%s, %s, %s, %s)
    """, ("API Admin", admin_email, hashed_password, True))

    conn.commit()
    cur.close()
    conn.close()

    print("🔥 Superusuário criado automaticamente!")