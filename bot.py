import json
import asyncio
import discord

from reminder import Reminder
from dice import RollDice
from pinner import Pinner

config = json.load(open('./config.json'))
loop = asyncio.get_event_loop()
client = discord.Client()

reminder = Reminder(loop)
dice = RollDice()
pinner = Pinner()

@client.event
async def on_ready():
	print("Bot is ready.")
	for ch in config['greet_ch']:
		channel = client.get_channel(ch)
		await channel.send('おはよう！')

@client.event
async def on_message(message):
	if message.author.bot:
		return
	
	print("Received message: " + message.content)

	if message.content.startswith(config['prefix'] + "remind"):
		# リマインダ
		await reminder.on_message(message)

	if message.content.startswith(config['prefix'] + "help"):
		# ヘルプ (README)
		await message.channel.send(f"{message.author.mention} {config['readme']}")

	elif message.content == "dicedice-dice":
		# サイコロ
		await dice.on_message(message)

	if message.channel.id in config['pin_ch']:
		await pinner.on_message(message)

client.run(config['token'])
loop.stop()
