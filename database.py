import sqlite3

DATABASE = "plbunny.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER NOT NULL,
            guild_id INTEGER NOT NULL,
            xp INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY (user_id, guild_id)
        )
    """)

    connection.commit()
    connection.close()


def get_user(user_id, guild_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT user_id, guild_id, xp
        FROM users
        WHERE user_id = ? AND guild_id = ?
    """, (user_id, guild_id))

    user = cursor.fetchone()
    connection.close()

    return user


def add_xp(user_id, guild_id, amount):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users (user_id, guild_id, xp)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id, guild_id)
        DO UPDATE SET xp = xp + ?
    """, (user_id, guild_id, amount, amount))

    connection.commit()
    connection.close()
