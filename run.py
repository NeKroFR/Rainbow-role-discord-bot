from config import *
import discord
import asyncio
import random

client = discord.Client(intents=discord.Intents.default())

async def rainbowroles():
    guild = await client.fetch_guild(SERVER_ID)
    for role in guild.roles:
            if str(role) in ROLES:
                print("detected role: " + "\033[95m" + str(role) + "\033[0m")

    while not client.is_closed():
        for role in guild.roles:
            if str(role) in ROLES:
                try:
                    await role.edit(color=random.choice(COLOURS))
                except Exception:
                    print("\033[31mcan't edit the role, make sure the bot's role is above the rainbow role and that it has permissions to edit roles\033[0")
        await asyncio.sleep(DELAY)                            

@client.event
async def on_ready():
    client.loop.create_task(rainbowroles())
    print("\033[32m--------------")
    print("Logged in as :")
    print(client.user.name)
    print(client.user.id)
    print("Ready.")
    print("--------------\033[0m")

client.run(TOKEN)
