import asyncio
import random
from ..my_decorator import decorator as deco

async def call_web_api(url) -> str:
    print(f"send a request: {url}")
    await asyncio.sleep(random.random())
    print(f"got a response: {url}")
    return f"{url}response"

async def async_download(url):
    response = await call_web_api(url)
    return response

async def task_test(n):
    await asyncio.sleep(n)
    return n

async def main():
    task = asyncio.gather(
        async_download("https://twitter.com/"),
        async_download("https://facebook.com/"),
        async_download("https://instagram.com/")
    )
    return await task

@deco.elapsed_time
async def generate_task():
    task1 = asyncio.create_task(task_test(1))
    task2 = asyncio.create_task(task_test(2))
    task3 = asyncio.create_task(task_test(3))
    print(await task1)
    print(await task2)
    print(await task3)


#result = asyncio.run(main())
asyncio.run(generate_task())