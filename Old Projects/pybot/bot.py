import discord


client = discord.Client()


@client.event
async def on_ready():
    print('Das Programm ist online mit dem Username {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!cat'):
        await message.channel.send('🐱')


    if message.content.startswith('!stop'):
        await message.channel.send('Der Bot wird nun gestoppt!')
        exit()


    if message.content.startswith('!help'):
        await message.channel.send('Hilfe zum PyBot')
        await message.channel.send('!cat - Du bekommst eine Katze')


    if message.content.startswith('Hallo'):
        await message.channel.send('Grüß Gott')
        await message.channel.send('Wilkommen am Server!')
        await message.channel.send('Bitte tippe !login ein, um dich anzumelden!')


    if message.content.startswith('!login'):
        await message.channel.send('Sie sind nun angemeldet. Mit !logout können sie sich abmelden')


    if message.content.startswith('!logout'):
        await message.channel.send('Bye Bye!')






client.run('ODE5MjkyNjMxOTk3MDg3ODM0.YEkfuQ.8VndRST7F2eXJgpqmDFHMFU4nCw')