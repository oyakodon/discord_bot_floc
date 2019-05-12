import discord
import re

class Pinner:
	def __init__(self):
		pass
	
	async def on_message(self, message):
		channel = message.channel

		pattern = "\[(.+)\].*"
		re_tag = re.match(pattern, message.content) # タグを検索
		
		for pinned in await channel.pins():
			re_pin_tag = re.match(pattern, pinned.content)
			if re_tag:
				# ピン留めメッセージに同じタグがついたものがあったらUnpin
				if re_pin_tag:
					if re_pin_tag.group(1) == re_tag.group(1):
						await pinned.unpin()
						break
			
			elif not re_pin_tag:
				# ピン留めメッセージに投稿者のものがあったらUnpin
				# (タグがついてなければ)
				if pinned.author == message.author:
					await pinned.unpin()
					break
		
		# ピン留め
		await message.pin()

		print("Message pinned.")

