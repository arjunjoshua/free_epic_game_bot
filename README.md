A Discord bot that checks in with the Epic Games API to tell you what the free game is that week!
Currently available as a custom bot that you can host yourself, but I plan to release it on Discord soon.

## Setting up 
1) Go to the Discord Developer Portal - https://discord.com/developers/applications
2) Create a new application and create a bot within the application. Make sure you copy the token
3) Go to the OAuth2 section and generate an invite link. Use this invite link to add the bot to your server.


## Using the bot
1) Add your desired channel ID and token from Step 2 of setting up as environment variables
2) Host the bot on a computer/server of your choice
3) Schedule the epic_games_bot.py file to run every Thursday after 16:00/17:00 GMT (The  resets at 11:00ET, so depends on daylight savings) 
