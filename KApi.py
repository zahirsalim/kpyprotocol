from KProtocol import KurentoProtocol

'''
Usage:
async def main():
    kur = await KurentoApi.createKurento()
'''

class KurentoApi(object):

    '''
    This Class will Use the KurentoProtocol to implement
    the KurentoAPI. Using the Factory Pattern as suggested by
    asyncio experts. The user is responsible for parsing the responses
    and handling success or failure. Idea is to abstract out the core api
    from specifics of the artifact generated on invoking the same
    '''
    
    @classmethod
    async def createKurento(cls):
        self = KurentoApi()
        self.kurento = await KurentoProtocol()
        return self

    async def ping(self):
        response = await self.kurento.request("ping")
        return response

    async def create(self,*args):
        response = await self.kurento.request("create",*args)
        return response

    async def invoke(self,*args):
        response = await self.kurento.request("invoke",*args)
        return response

    async def release(self,*args):
        response = await self.kurento.request("release",*args)
        return response

    async def subscribe(self,*args):
        response = await self.kurento.request("subscribe",*args)
        return response

    async def unsubscribe(self,*args):
        response = await self.kurento.request("unsubscribe",*args)
        return response

    async def onevent(self,*args):
        response = await self.kurento.request("onevent",*args)
        return response

