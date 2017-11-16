import discord
import asyncio
import python.wow_apis
import python.hearthstone_apis

# The bot client
client = discord.Client()

wow = python.wow_apis.WowApis()
hs = python.hearthstone_apis.HearthstoneApis()


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

        # If someone calls "/ilevel" or "/ilvl"
        if message.content.startswith("/ilevel") or message.content.startswith("/ilvl"):
            await wow_ilevel(message)

        # If someone calls "/card" or "/hs"
        if message.content.startswith("/card") or message.content.startswith("/hs"):
            await hearthstone_card(message)


async def help(message):
    """
    Writes what the bot can do
    """

    msg = "I don't have any functionality yet; just a friendly face."

    await client.send_message(message.channel, msg)


async def wow_ilevel(message):
    """
    Splits a message into ["/ilevel", <character>, <server>]
    Calls website_apis.wow_item_level() for the API call and information
    """

    command = message.content.split(" ")

    # If valid number of args
    if len(command) == 3:

        # Make the API call, which handles invalid input
        await client.send_message(message.channel, wow.ilevel(command[1], command[2]))

    else:
        await client.send_message(message.channel, "Error: Invalid number of arguments")


async def hearthstone_card(message):
    """
    Splits a message into ["/card", <card>]
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
