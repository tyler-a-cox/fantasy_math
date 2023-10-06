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