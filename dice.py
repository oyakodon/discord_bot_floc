import discord
import random

class RollDice:
	def __init__(self):
		self.tbl = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']

	async def on_message(self, message):
		dice = "{}{}-{}".format(random.choice(self.tbl), random.choice(self.tbl), random.choice(self.tbl))
		content = "{} {}".format(message.author.mention, dice)
		msg = await message.channel.send(content)
		if dice == "⚂⚂-⚃":
			emoji = '\N{PARTY POPPER}' # :tada:
			await msg.add_reaction(emoji)
		
