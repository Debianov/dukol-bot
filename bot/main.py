import os
from discord.ext import commands, tasks
from discord import Embed, Intents
from typing import Final, Any
import asyncio

class DukolBot(commands.Bot):

  async def on_ready(self):
    await self.load_extension('notificator')

if __name__ == '__main__':
  intents = Intents.all()
  bot = DukolBot(command_prefix="d ", intents=intents)
  bot.run(token=os.environ['DISCORD_TOKEN'])