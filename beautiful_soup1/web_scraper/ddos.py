import aiohttp
import asyncio

async def fetch(session, url, counter):
    async with session.get(url) as response:
        print(f"Request {counter} - Status Code: {response.status}")
        return await response.text()

async def make_requests_concurrently():
    url = "https://www.phunuonline.com.vn/"
    tasks = []

    # Configure connector with a higher limit for concurrent connections
    connector = aiohttp.TCPConnector(limit=5000)  # Adjust limit based on your needs

    async with aiohttp.ClientSession(connector=connector) as session:
        for counter in range(5000):  # Adjust the number of requests you want to make
            tasks.append(fetch(session, url, counter))
        await asyncio.gather(*tasks)

asyncio.run(make_requests_concurrently())
