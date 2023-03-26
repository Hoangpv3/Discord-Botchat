import discord
import handle
#from discord.ext import commands

TOKEN = 'MTA4ODQ4NTMxOTI5NDMyNDczNw.GsW6OK.LzdumBmPyUJte2Dt5Hu1ZWg4RWbpbmIXOcYAsE'
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents) #Bot vs Client

# Send messages
async def send_message(message, user_message, is_private, client):
    try:
        response = handle.handle_response(user_message, client)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():



    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(message)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")


        # If the user message contains a '?' in front of the text, it becomes a private message
        if user_message[0] == '?':
            user_message = user_message[1:]  # [1:] Removes the '?'
            await send_message(message, user_message, is_private=True, client=client)
        else:
            await send_message(message, user_message, is_private=False, client=client)







    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)