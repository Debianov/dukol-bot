import os
from discord import commands
from discord import tasks
import steam

discord_token = os.environ['DISCORD_TOKEN']

class BasedCog(commands.Cog):

  def __init__(self) -> None:
    self.new_part_msg: str = ""
    self.last_msg: str = ""

  @tasks.loop(hours=1)
  def update_checker(self) -> None:
    msg_to_analyze = steam.gather_data("1066780", "3069740688714545717")
    if self.last_message:
      self.last_msg = msg_to_analyze
      return
    if not msg_to_anaylyze == self.last_message:
      self.new_part_msg = 

if __name__ == '__main__':
  asyncio.run(gather_data())