import json
import os
import random

import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

with open("prompts.json", "r", encoding="utf-8") as file:
    prompt_data = json.load(file)

intents = discord.Intents.default()

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await tree.sync()
    print(f"plbunny is online as {client.user}")


@tree.command(name="prompt", description="Get a writing prompt.")
async def prompt(interaction: discord.Interaction):
    prompts = prompt_data["general"]
    selected = random.choice(prompts)

    await interaction.response.send_message(
        f"🐇 **Writing Prompt #{selected['id']}**\n\n"
        f"{selected['prompt']}"
    )


client.run(TOKEN)
