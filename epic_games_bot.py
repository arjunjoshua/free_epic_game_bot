#!/usr/bin/env python3

import discord
from discord.ext import commands
from get_epic_game import get_epic_game
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_BOT_TOKEN")
update_frequency = os.getenv("UPDATE_FREQUENCY")

# read channel ids from the channel_ids.txt file
with open("channel_ids.txt", "r") as f:
    channel_ids_from_file = [int(line.strip()) for line in f]

# Create a discord client
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    # # get the current free game
    # current_free_game = get_epic_game()
    #
    # if current_free_game:
    #     # send the current free game to the channel
    #     await send_to_channel(current_free_game)


@client.command()
async def free_game(ctx):
    # get the current free game
    current_free_game = get_epic_game()

    if current_free_game:
        # send the current free game to the channel
        await send_to_channel(current_free_game, [ctx.channel.id])

    else:
        await ctx.send(current_free_game)


@client.command()
async def subscribe_to_free_game(ctx):
    # check if the channel id is already in the list
    if ctx.channel.id in channel_ids_from_file:
        await ctx.send("You are already subscribed to free game updates.")
        return

    # save the channel id to the .txt file
    channel_ids_from_file.append(ctx.channel.id)
    with open("channel_ids.txt", "a") as f:
        f.write(f"{ctx.channel.id}\n")

    await ctx.send("You have successfully subscribed to free game updates.")


@client.command
async def unsubscribe_from_free_game(ctx):
    # check if the channel id is already in the list
    if ctx.channel.id not in channel_ids_from_file:
        await ctx.send("You are not subscribed to free game updates.")
        return

    # remove the channel id from the list
    channel_ids_from_file.remove(ctx.channel.id)
    with open("channel_ids.txt", "w") as f:
        for channel_id in channel_ids_from_file:
            f.write(f"{channel_id}\n")

    await ctx.send("You have successfully unsubscribed from free game updates.")


# send data to a channel
async def send_to_channel(current_free_game, channel_ids=None):
    if not channel_ids:
        channel_ids=channel_ids_from_file

    promo_end_date = datetime.datetime.strptime(current_free_game["promo_end_date"], "%Y-%m-%dT%H:%M:%S.%fZ")

    promo_end_date_formatted = promo_end_date.strftime("%B %d, %Y")

    message = f"This week's free game: {current_free_game['game_name']}\n\n Available until {promo_end_date_formatted}"

    embed = discord.Embed(title=current_free_game["game_name"], url=current_free_game["game_url"],
                          description=current_free_game["description"], color=0x00ff00)
    embed.set_image(url=current_free_game["image_url"])

    for channel_id in channel_ids:
        channel = client.get_channel(channel_id)
        if channel:
            await channel.send(message, embed=embed)

# start the bot
client.run(token)

