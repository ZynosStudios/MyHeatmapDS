import discord

client = discord.Client()

cmd_prefix = "$hmb"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(cmd_prefix):
        stripped_message = strip_prefix(message)
        command, arguments = message_to_command(stripped_message)

        if command == "echo":
            await message.channel.send(arguments[0])

        if command == "ping":
            await message.channel.send(":ping_pong: Pong!")

        if command == "region":
            pass


def check_authorization(message_author):
    pass


def message_to_command(stripped_message):
    split_message = stripped_message.split(' ')
    command = split_message[0]
    command.lower()
    arguments = split_message
    arguments.pop(0)
    return command, arguments


def strip_prefix(message):
    prefix_len = len(cmd_prefix) + 1
    return message.content[prefix_len:]


def run():
    token_file = open("bot.txt")
    token = token_file.read()
    client.run(token)


if __name__ == "__main__":
    run()
