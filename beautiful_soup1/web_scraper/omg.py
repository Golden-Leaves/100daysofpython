import aiohttp
import asyncio
import time

async def fetch(session, url, counter):
    try:
        async with session.get(url) as response:
            print(f"Request {counter} - Status Code: {response.status}")
            return await response.text()
    except Exception as e:
        print(f"Request {counter} failed: {e}")
        return None

async def make_requests_concurrently():
    url = "https://www.phunuonline.com.vn/"
    num_requests = 5000
    max_concurrent_requests = 1000  # Adjust based on system and network capacity

    # Use a semaphore to limit concurrency
    semaphore = asyncio.Semaphore(max_concurrent_requests)

    async def limited_fetch(counter):
        async with semaphore:
            return await fetch(session, url, counter)

    tasks = []
    # Use TCPConnector for connection pooling
    connector = aiohttp.TCPConnector(limit_per_host=max_concurrent_requests, use_dns_cache=True)

    start_time = time.time()
    async with aiohttp.ClientSession(connector=connector) as session:
        for counter in range(num_requests):
            tasks.append(limited_fetch(counter))

        # Run tasks concurrently
        await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"Completed {num_requests} requests in {end_time - start_time:.2f} seconds.")

# Run the script
asyncio.run(make_requests_concurrently())