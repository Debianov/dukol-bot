import os
from discord.ext import commands
from discord import Intents
from web_server import keep_alive

class DukolBot(commands.Bot):

  async def on_ready(self):
    keep_alive()
    await self.load_extension('notificator')

if __name__ == '__main__':
  intents = Intents.all()
  bot = DukolBot(command_prefix="d ", intents=intents)
  bot.run(token=os.environ['DISCORD_TOKEN'])