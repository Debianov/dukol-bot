import os
from discord.ext import commands, tasks
from discord import Embed, Intents
import steam
import discord
from typing import Final, Any, List, Optional, Union

class DukolBot(commands.Bot):
  
  def __init__(self, target_channel_id: int, *args: Any, **kwargs: Any) -> None:
    super().__init__(*args, **kwargs)
    self.target_channel_id = target_channel_id

  async def setup_hook(self) -> None:
    await self.add_cog(UpdateCog(self, self.target_channel_id))

class UpdateCog(commands.Cog):

  def __init__(self, bot: discord.Client, target_channel_id: int) -> None:
    self.bot = bot
    # self.update_checker.start()
    self.new_part_msg: str = ""
    self.len_last_msg: int = -1

  @commands.command()
  async def start(self, ctx: commands.Context) -> None:
    self.target_channel: discord.TextChannel = self.get_text_channel(target_channel_id)

  def get_text_channel(self, channel_id: int) -> discord.TextChannel:
    print(self.bot.guilds)
    maybe_text_channel = self.bot.get_channel(channel_id)
    print(maybe_text_channel)
    if isinstance(maybe_text_channel, discord.TextChannel):
      return maybe_text_channel
    return DummyTextChannel()

  @tasks.loop(seconds=1)
  async def update_checker(self) -> None:
    msg_to_analyze = await steam.gather_data("516750", "3069740688714545717")
    self.new_part_msg = msg_to_analyze
    await self.send_update_notification()
    if self.len_last_msg == -1:
        self.last_msg = len(msg_to_analyze)
    else:
      if self.len_last_msg < len(msg_to_analyze):
        self.new_part_msg = msg_to_analyze[self.len_last_msg:]
  
  async def send_update_notification(self) -> None:
    if self.new_part_msg:
      notification_embed = Embed()
      notification_embed.add_field(name="повідомлення", value=self.new_part_msg)
      await self.target_channel.send(embed=notification_embed)
      self.new_part_msg = ""

class DummyTextChannel(discord.TextChannel):
  
  def __init__(self) -> None:
    pass

if __name__ == '__main__':
  intents = Intents.all()
  target_channel_id: int = 792679070008606753
  dukol = DukolBot(target_channel_id, command_prefix="d ", intents=intents)
  dukol.run(token=os.environ['DISCORD_TOKEN'])