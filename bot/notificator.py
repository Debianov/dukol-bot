import os
from discord.ext import commands, tasks
from discord import Embed, Intents
import steam
from typing import Final, Any
import asyncio

class UpdateNotificator(commands.Cog):
  
  def __init__(self, bot: commands.Bot, channel_id: int) -> None:
    self.bot = bot
    self.target_channel = self.bot.get_channel(channel_id)
    self.len_last_msg: int = -1

  async def cog_load(self) -> None:
    self.update_checker.start()

  @tasks.loop(seconds=5.0)
  async def update_checker(self) -> None:
    msg_to_analyze = await steam.gather_data("516750", "3069740688714545717")
    if self.len_last_msg < len(msg_to_analyze):
      await self.send_update_notification(msg_to_analyze[self.len_last_msg:])
    self.len_last_msg = len(msg_to_analyze)
  
  async def send_update_notification(self, msg_text: str) -> None:
    notification_embed = Embed()
    notification_embed.add_field(name="повідомлення", value=msg_text)
    await self.target_channel.send(embed=notification_embed)

async def setup(bot):
  target_channel = 792679070008606753
  await bot.add_cog(UpdateNotificator(bot, target_channel))