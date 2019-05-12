import threading
import time
from datetime import datetime
import sched
import asyncio
import discord

class Reminder:
	def __init__(self, loop):
		self.loop = loop

	def send_remind(self, channel, body):
		asyncio.ensure_future(channel.send(body), loop=self.loop)
		print("Reminder done.")

	def remind(self, channel, delay, body):
		scheduler = sched.scheduler(time.time, time.sleep)
		scheduler.enter(delay, 1, self.send_remind, argument=(channel, body))
		scheduler.run()

	async def on_message(self, message):
		channel = message.channel

		# コマンド解析
		s = message.content.split(' ')
		if len(s) < 5:
			await channel.send(':no_good: 引数の数が足りないっぽい')
			return
		try:
			format = '%Y-%m-%d %H:%M:%S' if len(s[2]) > 5 else '%Y-%m-%d %H:%M'
			dt = datetime.strptime(' '.join(s[1:3]), format)
		except:
			await channel.send(':no_good: 日時のフォーマットが違うっぽい')
			return
		delay = int((dt - datetime.now()).total_seconds())
		if delay < 0:
			await channel.send(':no_good: 過去の日時参照してない？')
			return

		# mention id 取得
		found = False
		## here or everyone
		if s[3] in ['here', 'everyone']:
			mention = '@' + s[3]
			found = True
		## Role走査
		for role in message.guild.roles:
			if role.name == s[3]:
				mention = role.mention
				found = True
		## User走査
		if message.guild.get_member_named(s[3]) != None:
			mention = message.guild.get_member_named(s[3]).mention
			found = True

		if not found:
			await channel.send(':no_good: 指定されたユーザが存在しないみたい')
			return
		
		body = f"{mention}\r[リマインダ]\r{s[4]}"

		# スレッド作成
		thread = threading.Thread(target=self.remind, args=(channel, delay, body))
		thread.start()

		print("Reminder registed.")
		await channel.send(':ok_woman: リマインダに登録したよ')
