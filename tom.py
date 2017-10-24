import discord
import asyncio


# The bot client
client = discord.Client()


@client.event
async def on_ready():
    """
    When the bot signs in

    This function runs when the bot first signs in. Print statements only show in the terminal, like they usually would,
    and are basically just for testing purposes. The channel_id is the ID of a specific channel; in this case it's the
    "bot_testing" channel on our server, so it can post a message when it comes online.
    """

    print("%s (ID: %s) logged in" % (client.user.name, client.user.id))
    print("----------------------------------------")

    # "bot_testing" chat channel id
    channel_id = "369349307897217024"

    # Post a message when the bot comes online
    msg = "Tom is online. Hello!"
    await client.send_message(client.get_channel(channel_id), msg)

    # Set the bot's "Playing" status
    await client.change_presence(game=discord.Game(name="Type !help"))


@client.event
async def on_message(message):
    """
    When messages are posted

    This function runs whenever someone posts a message, in any channel that is visible to the bot. "message.content" is
    the message as a String, which we can use regular Python on. I left "/help" as an example command.
    """

    # Prevent the bot from responding to itself
    if message.author != client.user:

        # If someone calls "/help"
        if message.content.startswith("/help"):
            await help(message)


async def help(message):
    """
    Writes what the bot can do
    """

    msg = "I don't have any functionality yet; just a friendly face."

    await client.send_message(message.channel, msg)


# Run the bot
#client.run("INSERT TOKEN HERE")
client.run("MzcyNTI4NjYxMDIwMjc4Nzg3.DNFjfA.6pTgO9hw7XqGzVgNdRFdikPBlBQ")