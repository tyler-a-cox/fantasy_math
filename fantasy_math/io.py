import asyncio
import aiohttp
import pandas as pd

async def fetch_html(session, url):
    """
    """
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()
    except aiohttp.ClientError as e:
        print(f"Error fetching {url}: {e}")
        return None

async def read_html(urls):
    """
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_html(session, url) for url in urls]
        html_contents = await asyncio.gather(*tasks)

    tables = []
    # Parse the HTML content using pd.read_html
    for html_content in html_contents:
        if html_content is not None:
            try:
                tables.append(pd.read_html(html_content))
            except pd.errors.EmptyDataError:
                print("No data found in HTML.")
    
    return tables

def get_fantasy_urls(year_range=[2015, 2023], week_range=[1, 17], players=['qb', 'rb', 'wr', 'te']):
    """
    """
    urls = [] 
    for yi in range(year_range):
        for wi in range(week_range):
            for player_label in range(players):
                url = f"https://www.footballguys.com/playerhistoricalstats?pos={player_label}&yr={yi}&startwk={wi}&stopwk={wi}&profile=p"
                urls.append(url)

    return urls

def transform_tables():
    """
    """
    pass
