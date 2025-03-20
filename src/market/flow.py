import asyncio
import json

import websockets

from src.core.config import get_settings

settings = get_settings()
TD_API_KEY = settings.TD_API_KEY


async def websocket_client():
    url = f"wss://ws.twelvedata.com/v1/quotes/price?apikey={TD_API_KEY}"

    async with websockets.connect(url) as websocket:
        subscribe_message = {
            "action": "subscribe",
            "params": {"symbols": "AAPL,RY,RY:TSX,EUR/USD,BTC/USD"},
        }
        await websocket.send(json.dumps(subscribe_message))

        while True:
            response = await websocket.recv()
            data = json.loads(response)
            print("Received:", data)


# WebSocket 클라이언트 실행
if __name__ == "__main__":
    asyncio.run(websocket_client())
