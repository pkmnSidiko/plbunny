DEFAULT_CONFIG = {
    "timezone": "UTC",
    "xp_enabled": True,
    "announcement_channel_id": None,
    "writing_channel_id": None,
}


def get_default_config():
    return DEFAULT_CONFIG.copy()
