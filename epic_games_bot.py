#!/usr/bin/env python3

import discord
from get_epic_game import get_epic_game
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_BOT_TOKEN")
channel_id = os.getenv("CHANNEL_ID")
update_frequency = os.getenv("UPDATE_FREQUENCY")

# Create a discord client
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
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

    promo_end_date = datetime.datetime.strptime(current_free_game["promo_end_date"], "%Y-%m-%dT%H:%M:%S.%fZ")

    promo_end_date_formatted = promo_end_date.strftime("%B %d, %Y")

    message = f"This week's free game: {current_free_game['game_name']}\n\n Available until {promo_end_date_formatted}"

    embed = discord.Embed(title=current_free_game["game_name"], url=current_free_game["game_url"],
                          description=current_free_game["description"], color=0x00ff00)
    embed.set_image(url=current_free_game["image_url"])

    if channel:
        await channel.send(message, embed=embed)

    # close the connection
    await client.close()


# start the bot
client.run(token)

