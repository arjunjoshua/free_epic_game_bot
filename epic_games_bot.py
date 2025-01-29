#!/usr/bin/env python3

import discord
from get_epic_game import get_epic_game
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_BOT_TOKEN")
channel_id = os.getenv("CHANNEL_ID")

# Create a discord client
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    # get the current free game
    current_free_game = get_epic_game()

    if current_free_game:
        # send the current free game to the channel
        await send_to_channel(current_free_game)


# send data to a channel
async def send_to_channel(current_free_game):
    channel = client.get_channel(int(channel_id))
    date = datetime.datetime.now()

    # Get the next Thursday's date
    while date.weekday() != 3:
        date += datetime.timedelta(days=1)

    date_in_one_week_formatted = date.strftime("%b %d, %Y") + " 16:00 UTC"

    message = f"This week's free game: {current_free_game['game_name']}\n\n Available until {date_in_one_week_formatted}"

    embed = discord.Embed(title=current_free_game["game_name"], url=current_free_game["game_url"],
                          description="Available until {date_in_one_week}")
    embed.set_image(url=current_free_game["image_url"])

    if channel:
        await channel.send(message, embed=embed)

    # close the connection
    await client.close()


# start the bot
client.run(token)

