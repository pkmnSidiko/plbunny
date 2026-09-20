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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS guild_config (
            guild_id INTEGER PRIMARY KEY,
            timezone TEXT NOT NULL DEFAULT 'UTC',
            xp_enabled INTEGER NOT NULL DEFAULT 1,
            announcement_channel_id INTEGER,
            writing_channel_id INTEGER
        )
    """)

    connection.commit()
    connection.close()


def get_guild_config(guild_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT guild_id, timezone, xp_enabled,
               announcement_channel_id, writing_channel_id
        FROM guild_config
        WHERE guild_id = ?
    """, (guild_id,))

    config = cursor.fetchone()
    connection.close()

    return config

def save_guild_config(
    guild_id,
    timezone="UTC",
    xp_enabled=True,
    announcement_channel_id=None,
    writing_channel_id=None
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO guild_config (
            guild_id,
            timezone,
            xp_enabled,
            announcement_channel_id,
            writing_channel_id
        )
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(guild_id)
        DO UPDATE SET
            timezone = excluded.timezone,
            xp_enabled = excluded.xp_enabled,
            announcement_channel_id = excluded.announcement_channel_id,
            writing_channel_id = excluded.writing_channel_id
    """, (
        guild_id,
        timezone,
        int(xp_enabled),
        announcement_channel_id,
        writing_channel_id
    ))

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


def set_guild_config(guild_id, setting, value):
    connection = get_connection()
    cursor = connection.cursor()

    allowed_settings = {
        "timezone",
        "xp_enabled",
        "announcement_channel_id",
        "writing_channel_id",
    }

    if setting not in allowed_settings:
        connection.close()
        raise ValueError(f"Unknown guild setting: {setting}")

    cursor.execute(
        f"""
        UPDATE guild_config
        SET {setting} = ?
        WHERE guild_id = ?
        """,
        (value, guild_id)
    )

    connection.commit()
    connection.close()