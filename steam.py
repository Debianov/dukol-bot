import json
from bs4 import BeautifulSoup
import asyncio
import aiohttp
from typing import List

async def gather_data(app_id, disc_id):
    url = f'https://steamcommunity.com/app/{app_id}/discussions/0/{disc_id}'
    header = {
      'Accept': '*/*',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'ru,en;q=0.9,ru-RU;q=0.8,en-US;q=0.7',
      'Connection': 'keep-alive'
    }
    async with aiohttp.ClientSession() as session:
      response = await session.get(url=url, headers=header)
      soup = BeautifulSoup(await response.text(), 'html.parser')
      discussion = soup.find(id=f"forum_op_{disc_id}")
      top_message = discussion.find(class_="content")

if __name__ == '__main__':
  asyncio.run(gather_data("1066780", "3069740688714545717"))