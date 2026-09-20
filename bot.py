import json
import os
import random
from typing import Optional
from zoneinfo import ZoneInfo

import discord
from discord import app_commands
from dotenv import load_dotenv

from database import (
    initialize_database,
    get_user,
    add_xp,
    set_guild_config,
)
from config import get_guild_config

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CONFIG = {}

TEST_GUILD = discord.Object(id=1550916613404885002)

initialize_database()

with open("prompts.json", "r", encoding="utf-8") as file:
    prompt_data = json.load(file)

intents = discord.Intents.default()

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# --------------------------------------------------
# Configuration command group
# --------------------------------------------------

config_group = app_commands.Group(
    name="config",
    description="Configure Plotbunny for this server."
)

tree.add_command(config_group)


def is_admin(interaction: discord.Interaction):
    """Return True if the user has administrator permissions."""
    return (
        interaction.guild is not None
        and isinstance(interaction.user, discord.Member)
        and interaction.user.guild_permissions.administrator
    )


def get_current_config(interaction: discord.Interaction):
    """Load configuration for the server where the command was used."""
    if interaction.guild is None:
        return None

    return get_guild_config(interaction.guild.id)


# --------------------------------------------------
# Bot startup
# --------------------------------------------------

@client.event
async def on_ready():
    guild = TEST_GUILD

    global CONFIG
    CONFIG = get_guild_config(guild.id)

    print("Loaded server config:", CONFIG)

    tree.clear_commands(guild=guild)
    tree.copy_global_to(guild=guild)

    synced = await tree.sync(guild=guild)

    print("Synced guild commands:", [command.name for command in synced])

    print(f"plbunny is online as {client.user}")


# --------------------------------------------------
# /prompt
# --------------------------------------------------

@tree.command(
    name="prompt",
    description="Get a writing prompt."
)
async def prompt(interaction: discord.Interaction):
    prompts = prompt_data["general"]
    selected = random.choice(prompts)

    await interaction.response.send_message(
        f"🐇 **Writing Prompt #{selected['id']}**\n\n"
        f"{selected['prompt']}"
    )


# --------------------------------------------------
# /xp
# --------------------------------------------------

@tree.command(
    name="xp",
    description="Check your current XP."
)
async def xp(interaction: discord.Interaction):
    config = get_current_config(interaction)

    if config is None:
        await interaction.response.send_message(
            "🐇 This command can only be used inside a server.",
            ephemeral=True
        )
        return

    if not config["xp_enabled"]:
        await interaction.response.send_message(
            "🐇 XP is currently disabled in this server.",
            ephemeral=True
        )
        return

    user = get_user(
        interaction.user.id,
        interaction.guild.id
    )

    current_xp = user[2] if user else 0

    await interaction.response.send_message(
        f"🐇 **{interaction.user.display_name}**\n"
        f"XP: **{current_xp}**"
    )


# --------------------------------------------------
# /give_xp
# --------------------------------------------------

@tree.command(
    name="give_xp",
    description="Give a user XP."
)
@app_commands.describe(
    member="The member receiving XP.",
    amount="The amount of XP to award."
)
async def give_xp(
    interaction: discord.Interaction,
    member: discord.Member,
    amount: int
):
    config = get_current_config(interaction)

    if config is None:
        await interaction.response.send_message(
            "🐇 This command can only be used inside a server.",
            ephemeral=True
        )
        return

    if not config["xp_enabled"]:
        await interaction.response.send_message(
            "🐇 XP is currently disabled in this server.",
            ephemeral=True
        )
        return

    if not interaction.user.guild_permissions.manage_guild:
        await interaction.response.send_message(
            "🐇 You need the **Manage Server** permission to award XP.",
            ephemeral=True
        )
        return

    if amount <= 0:
        await interaction.response.send_message(
            "🐇 XP must be greater than 0.",
            ephemeral=True
        )
        return

    add_xp(
        member.id,
        interaction.guild.id,
        amount
    )

    await interaction.response.send_message(
        f"🐇 **{member.display_name}** received **{amount} XP**!"
    )


# --------------------------------------------------
# /config show
# --------------------------------------------------

@config_group.command(
    name="show",
    description="Show Plotbunny's configuration for this server."
)
async def config_show(interaction: discord.Interaction):
    if not is_admin(interaction):
        await interaction.response.send_message(
            "🐇 You need Administrator permission to view Plotbunny's configuration.",
            ephemeral=True
        )
        return

    config = get_current_config(interaction)

    if config is None:
        await interaction.response.send_message(
            "🐇 This command can only be used inside a server.",
            ephemeral=True
        )
        return

    xp_status = "Enabled" if config["xp_enabled"] else "Disabled"

    if config["announcement_channel_id"] is None:
        announcement_channel = "Not configured"
    else:
        announcement_channel = f"<#{config['announcement_channel_id']}>"

    if config["writing_channel_id"] is None:
        writing_channel = "Not configured"
    else:
        writing_channel = f"<#{config['writing_channel_id']}>"

    embed = discord.Embed(
        title="🐇 Plotbunny Configuration",
        description="Current server-specific settings."
    )

    embed.add_field(
        name="Timezone",
        value=config["timezone"],
        inline=False
    )

    embed.add_field(
        name="XP",
        value=xp_status,
        inline=True
    )

    embed.add_field(
        name="Writing Channel",
        value=writing_channel,
        inline=True
    )

    embed.add_field(
        name="Announcement Channel",
        value=announcement_channel,
        inline=True
    )

    await interaction.response.send_message(
        embed=embed,
        ephemeral=True
    )


# --------------------------------------------------
# /config writing-channel
# --------------------------------------------------

@config_group.command(
    name="writing-channel",
    description="Set or clear the server's writing channel."
)
@app_commands.describe(
    channel="The channel Plotbunny should recognize as the writing channel."
)
async def config_writing_channel(
    interaction: discord.Interaction,
    channel: Optional[discord.TextChannel] = None
):
    if not is_admin(interaction):
        await interaction.response.send_message(
            "🐇 You need Administrator permission to change Plotbunny's configuration.",
            ephemeral=True
        )
        return

    if interaction.guild is None:
        await interaction.response.send_message(
            "🐇 This command can only be used inside a server.",
            ephemeral=True
        )
        return

    if channel is None:
        set_guild_config(
            interaction.guild.id,
            "writing_channel_id",
            None
        )

        await interaction.response.send_message(
            "🐇 The writing channel has been cleared.",
            ephemeral=True
        )
        return

    set_guild_config(
        interaction.guild.id,
        "writing_channel_id",
        channel.id
    )

    await interaction.response.send_message(
        f"🐇 Writing channel set to {channel.mention}.",
        ephemeral=True
    )


# --------------------------------------------------
# /config announcement-channel
# --------------------------------------------------

@config_group.command(
    name="announcement-channel",
    description="Set or clear the server's announcement channel."
)
@app_commands.describe(
    channel="The channel Plotbunny should use for announcements."
)
async def config_announcement_channel(
    interaction: discord.Interaction,
    channel: Optional[discord.TextChannel] = None
):
    if not is_admin(interaction):
        await interaction.response.send_message(
            "🐇 You need Administrator permission to change Plotbunny's configuration.",
            ephemeral=True
        )
        return

    if interaction.guild is None:
        await interaction.response.send_message(
            "🐇 This command can only be used inside a server.",
            ephemeral=True
        )
        return

    if channel is None:
        set_guild_config(
            interaction.guild.id,
            "announcement_channel_id",
            None
        )

        await interaction.response.send_message(
            "🐇 The announcement channel has been cleared.",
            ephemeral=True
        )
        return

    set_guild_config(
        interaction.guild.id,
        "announcement_channel_id",
        channel.id
    )

    await interaction.response.send_message(
        f"🐇 Announcement channel set to {channel.mention}.",
        ephemeral=True
    )


# --------------------------------------------------
# /config timezone
# --------------------------------------------------

@config_group.command(
    name="timezone",
    description="Set the server's timezone."
)
@app_commands.describe(
    timezone="IANA timezone, such as America/New_York."
)
async def config_timezone(
    interaction: discord.Interaction,
    timezone: str
):
    if not is_admin(interaction):
        await interaction.response.send_message(
            "🐇 You need Administrator permission to change Plotbunny's configuration.",
            ephemeral=True
        )
        return

    if interaction.guild is None:
        await interaction.response.send_message(
            "🐇 This command can only be used inside a server.",
            ephemeral=True
        )
        return

    try:
        ZoneInfo(timezone)
    except Exception:
        await interaction.response.send_message(
            "🐇 I don't recognize that timezone.\n\n"
            "Use an IANA timezone such as `America/New_York`, "
            "`America/Chicago`, or `Europe/London`.",
            ephemeral=True
        )
        return

    set_guild_config(
        interaction.guild.id,
        "timezone",
        timezone
    )

    await interaction.response.send_message(
        f"🐇 Server timezone set to **{timezone}**.",
        ephemeral=True
    )


# --------------------------------------------------
# /config xp
# --------------------------------------------------

@config_group.command(
    name="xp",
    description="Enable or disable XP for this server."
)
@app_commands.describe(
    enabled="Whether XP should be enabled."
)
async def config_xp(
    interaction: discord.Interaction,
    enabled: bool
):
    if not is_admin(interaction):
        await interaction.response.send_message(
            "🐇 You need Administrator permission to change Plotbunny's configuration.",
            ephemeral=True
        )
        return

    if interaction.guild is None:
        await interaction.response.send_message(
            "🐇 This command can only be used inside a server.",
            ephemeral=True
        )
        return

    set_guild_config(
        interaction.guild.id,
        "xp_enabled",
        int(enabled)
    )

    status = "enabled" if enabled else "disabled"

    await interaction.response.send_message(
        f"🐇 XP has been **{status}** for this server.",
        ephemeral=True
    )


# --------------------------------------------------
# Start bot
# --------------------------------------------------

client.run(TOKEN)