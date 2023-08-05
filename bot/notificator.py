import os
from discord.ext import commands, tasks
from discord import Embed, Intents
import steam
from typing import Final, Any
import asyncio

class UpdateNotificator(commands.Cog):
  
  def __init__(self, bot: commands.Bot, channel_id: int) -> None:
    self.bot = bot
    self.channel = self.bot.get_channel(channel_id)
    self.new_part_msg: str = ""
    self.len_last_msg: int = -1

  async def cog_load(self) -> None:
    self.update_checker.start()

  @tasks.loop(seconds=1.0)
  async def update_checker(self) -> None:
    msg_to_analyze = await steam.gather_data("516750", "3069740688714545717")
    self.new_part_msg = msg_to_analyze
    await self.send_update_notification()
    if self.len_last_msg == -1:
        self.len_last_msg = len(msg_to_analyze)
    else:
      if self.len_last_msg < len(msg_to_analyze):
        self.new_part_msg = msg_to_analyze[self.len_last_msg:]
  
  async def send_update_notification(self) -> None:
    if self.new_part_msg:
      notification_embed = Embed()
      notification_embed.add_field(name="повідомлення", value=self.new_part_msg)
      await self.target_channel.send(embed=notification_embed)
      self.new_part_msg = ""

async def setup(bot):
  target_channel = 792679070008606753
  await bot.add_cog(UpdateNotificator(bot, target_channel))