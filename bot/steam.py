from bs4 import BeautifulSoup
import asyncio
import aiohttp

async def gather_data(app_id: str, disc_id: str) -> str:
    url = f'https://steamcommunity.com/app/{app_id}/discussions/2/{disc_id}'
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
      return top_message