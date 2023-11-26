import aiohttp
import asyncio
import uuid


async def send_request(session):
    payload = {"uuid": str(uuid.uuid4())}
    print(f"Sending request with payload {payload}")
    async with session.post("http://127.0.0.1:8000/", json=payload) as response:
        print(f"Response for payload {payload} {await response.json()}")


async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[send_request(session) for _ in range(60)])


if __name__ == "__main__":
    asyncio.run(main())
