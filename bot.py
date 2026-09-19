import json
import os
import random

import discord
from discord import app_commands
from dotenv import load_dotenv

from database import initialize_database, get_user, add_xp

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

initialize_database()

with open("prompts.json", "r", encoding="utf-8") as file:
    prompt_data = json.load(file)

intents = discord.Intents.default()

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    guild = discord.Object(id=1550916613404885002)

    tree.copy_global_to(guild=guild)

    synced = await tree.sync(guild=guild)
    print("Synced guild commands:", [command.name for command in synced])

    print(f"plbunny is online as {client.user}")


@tree.command(name="prompt", description="Get a writing prompt.")
async def prompt(interaction: discord.Interaction):
    prompts = prompt_data["general"]
    selected = random.choice(prompts)

    await interaction.response.send_message(
        f"🐇 **Writing Prompt #{selected['id']}**\n\n"
        f"{selected['prompt']}"
    )

@tree.command(name="xp", description="Check your current XP.")
async def xp(interaction: discord.Interaction):
    user = get_user(interaction.user.id, interaction.guild.id)

    current_xp = user[2] if user else 0

    await interaction.response.send_message(
        f"🐇 **{interaction.user.display_name}**\n"
        f"XP: **{current_xp}**"
    )
@tree.command(name="give_xp", description="Give a user XP.")

async def give_xp(
    interaction: discord.Interaction,
    member: discord.Member,
    amount: int
):
    if amount <= 0:
        await interaction.response.send_message(
            "🐇 XP must be greater than 0.",
            ephemeral=True
        )
        return

    add_xp(member.id, interaction.guild.id, amount)

    await interaction.response.send_message(
        f"🐇 **{member.display_name}** received **{amount} XP**!"
    )

client.run(TOKEN)
