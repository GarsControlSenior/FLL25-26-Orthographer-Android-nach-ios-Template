from bleak import BleakScanner, BleakClient
import asyncio
from threading import Thread

class BLEManager:

    def __init__(self, app):
        self.app = app
        self.client = None

    def start_scan(self):
        Thread(target=self.scan).start()

    def scan(self):
        asyncio.run(self._scan())

    async def _scan(self):
        devices = await BleakScanner.discover()
        for d in devices:
            if "Arduino" in d.name:
                await self.connect(d)

    async def connect(self, device):
        self.client = BleakClient(device)
        await self.client.connect()
        self.app.ble_status = "Connected"