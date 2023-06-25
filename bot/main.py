import os
from discord.ext import commands, tasks
from discord import Embed, Intents
import steam
from typing import Final, Any

class DukolBot(commands.Bot):
  
  def __init__(self, channel_id: int, *args: Any, **kwargs: Any) -> None:
    super().__init__(*args, **kwargs)
    self.channel_id: int = channel_id
    self.new_part_msg: str = ""
    self.len_last_msg: int = -1

  async def setup_hook(self) -> None:
    self.channel = self.get_channel(self.channel_id)
    self.update_checker.start()

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
      await self.channel.send(embed=notification_embed)
      self.new_part_msg = ""

if __name__ == '__main__':
  intents = Intents.all()
  target_channel = 792679070008606753
  dukol = DukolBot(target_channel, command_prefix="d ", intents=intents)
  dukol.run(token=os.environ['DISCORD_TOKEN'])