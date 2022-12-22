import asyncio
import os

from foundation.client import TgClient


async def run_echo():
    c = TgClient(os.getenv("5808059076:AAGTYhIYT2sbkw06wQcnuVpupVmrmWxEhgA"))
    print(await c.get_updates(offset=0, timeout=5))


if __name__ == "__main__":
    asyncio.run(run_echo())
