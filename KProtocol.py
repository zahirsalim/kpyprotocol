import asyncio
import websockets
from jsonrpcclient.clients.websockets_client import WebSocketsClient

'''

Sample Usage of KurentoProtocol

async def main():
    async with KurentoProtol() as kurento:
        response = await kurento.request("ping")
        print(response)  # "Hello!"


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

'''

class KurentoProtocol(object):

    '''
    Encapsulates the jsonrpclient method to facilitate Kurento RPC
    '''
   
    async def __aenter__(self):
        self._conn = websockets.connect("ws://localhost:8888/kurento")
        self.websocket = await self._conn.__aenter__()
        return self

    async def __aexit__(self, *args, **kwargs):
        await self._conn.__aexit__(*args, **kwargs)

    async def request(self,method_name:str,**kwargs):
        response = await WebSocketsClient(self.websocket).request(method_name,**kwargs)
        return response.data
 

