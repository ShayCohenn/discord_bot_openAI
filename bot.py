import discord
import response

async def send_msg(msg, user_msg, is_private):
    """
    Send a response message to the user or the channel.

    Parameters:
        msg (discord.Message): The original message sent by the user.
        user_msg (str): The user's message content.
        is_private (bool): True if the response should be sent privately to the user,
        False otherwise.
    """
    try:
        res = response.get_res(user_msg)
        if is_private:
            await msg.author.send(res)
        else:
            await msg.channel.send(res)

    except Exception as exception:
        print(exception)

def read_token_from_file(file_path):
    """
    Read the Discord bot token from a file.

    Parameters:
        file_path (str): The path to the file containing the Discord bot token.

    Returns:
        str: The Discord bot token read from the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip()

def run_dis_bot():
    """
    Run the Discord bot with the provided token from the 'discord_token.txt' file.
    """
    token_file_path = "discord_token.txt"
    token = read_token_from_file(token_file_path)

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return
        username = str(msg.author)
        user_msg = str(msg.content)
        channel = str(msg.channel)

        print(f'{username} said: "{user_msg}" ({channel})')

        if user_msg.startswith('?'):
            user_msg = user_msg[1:]
            await send_msg(msg, user_msg, is_private=True)
        else:
            await send_msg(msg, user_msg, is_private=False)

    client.run(token)

if __name__ == "__main__":
    run_dis_bot()
