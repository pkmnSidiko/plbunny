from database import get_guild_config as get_saved_guild_config


DEFAULT_CONFIG = {
    "timezone": "UTC",
    "xp_enabled": True,
    "announcement_channel_id": None,
    "writing_channel_id": None,
}


def get_default_config():
    return DEFAULT_CONFIG.copy()


def get_guild_config(guild_id):
    config = get_saved_guild_config(guild_id)

    if config is None:
        return get_default_config()

    return {
        "guild_id": config[0],
        "timezone": config[1],
        "xp_enabled": bool(config[2]),
        "announcement_channel_id": config[3],
        "writing_channel_id": config[4],
    }