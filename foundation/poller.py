import asyncio

from foundation.client import TgClient


class Poller:
    def __init__(self, token: str, queue: asyncio.Queue):
        self.tg_client = TgClient(token)
        self.queue = queue

    async def _worker(self):
        offset = 0
        while True:
            res = await self.tg_client.get_updates_in_objects(offset=offset, timeout=60)
            for u in res.result:
                offset = u.update_id + 1
                print(u)
                self.queue.put_nowait(u)

    async def start(self):
        asyncio.create_task(self._worker())
