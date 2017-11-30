import discord
import asyncio
import wednesday
from wow_apis import WowApis
from hearthstone_apis import HearthstoneApis
import python.Spam_Controller

# The bot client
client = discord.Client()

# World Of Warcraft API
wow = WowApis()

# Hearthstone API
hs = HearthstoneApis()

#Spam Controller
spam_cont = python.Spam_Controller.Spam_Controller(5, 10, 2)


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

    # Get the "bot_testing" chat channel id
    id_file = open("../keys/channel_id", "r")
    channel_id = id_file.read().strip()
    id_file.close()

    # Post a message when the bot comes online
    msg = "Tom is online. Hello!"
    await client.send_message(client.get_channel(channel_id), msg)

    # Set the bot's "Playing" status
    await client.change_presence(game=discord.Game(name="Type /help"))

    # Start the Wednesday timer
    time = wednesday.time_until_wednesday()
    await asyncio.sleep(time)
    await post_wednesday()


@client.event
async def on_message(message):
    """
    When messages are posted

    This function runs whenever someone posts a message, in any channel that is visible to the bot. "message.content" is
    the message as a String, which we can use regular Python on. I left "/help" as an example command.
    """

    # Prevent the bot from responding to itself
    if message.author != client.user:

        #Check if spam
        isSpam =  spam_cont.check_spam(message.author.name, str(message.timestamp), message.content)
        if isSpam:
            await client.delete_message(message)

        # If someone calls "/help"
        if message.content.startswith("/help"):
            await help(message)

        # If someone calls "/ilevel" or "/ilvl"
        if message.content.startswith("/ilevel") or message.content.startswith("/ilvl"):
            await parse_wow(message, wow.item_level)

        # If someone calls "/mplus"
        if message.content.startswith("/mplus"):
            await parse_wow(message, wow.mythic_plus)

        # If someone calls "/wow"
        if message.content.startswith("/wow"):
            await parse_wow(message, wow.all)

        # If someone calls "/card" or "/hs"
        if message.content.startswith("/card") or message.content.startswith("/hs"):
            await hearthstone_card(message)


async def help(message):
    """
    Writes what the bot can do
    """

    msg = "I don't have any functionality yet; just a friendly face."

    await client.send_message(message.channel, msg)


async def post_wednesday():
    await client.send_message(client.get_channel("369349307897217024"),
                              "http://i1.kym-cdn.com/photos/images/newsfeed/001/091/264/665.jpg")

    # Start the new Wednesday timer
    time = 7 * 24 * 60 * 60
    await asyncio.sleep(time)
    await post_wednesday()


async def parse_wow(message, function):
    """
    Splits a message into ["/ilevel", <character>, <server>]
    Calls the passed-in WowApis function and posts the results
    """

    command = message.content.split(" ")

    # If valid number of args
    if len(command) == 3:

        # Make the API call, which handles invalid input
        await client.send_message(message.channel, function(command[1], command[2]))

    else:
        await client.send_message(message.channel, "Error: Invalid number of arguments")


async def hearthstone_card(message):
    """
    Splits a message into ["/card", <card>]
    Calls HearthstoneApis.card() for the API call and results
    """

    command = message.content.split(" ")
    output = ""

    # If valid number of args
    if len(command) >= 2:

        # Make the API call, which handles invalid input
        await client.send_message(message.channel, hs.card(" ".join(command[1:])))

    else:
        await client.send_message(message.channel, "Error: Invalid number of arguments")


# Get the token and run the bot
token_file = open("../keys/discord_token", "r")
discord_token = token_file.read().strip()
token_file.close()

client.run(discord_token)
