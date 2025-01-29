import discord
from get_epic_game import get_epic_game
import datetime

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
    channel = client.get_channel(CHANNEL_ID)
    current_date = datetime.datetime.now().strftime("%b %d, %Y")
    date_in_one_week = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%b %d, %Y")

    # Get the next Thursday's date
    while datetime.datetime.now().weekday() != 3:
        date_in_one_week = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%b %d, %Y")

    # set the date in one week to 16:00 UTC
    date_in_one_week = f"{date_in_one_week} 16:00 UTC"

    message = f"This week's free game: {current_free_game['game_name']}\n\n Available until {date_in_one_week}"
    image_url = current_free_game['image_url']

    embed = discord.Embed(title=current_free_game["game_name"], url=current_free_game["game_url"], description="Available until {date_in_one_week}")

    if channel:
        await channel.send(message, embed=embed)

    # close the connection
    await client.close()

