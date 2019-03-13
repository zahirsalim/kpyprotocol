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

    Parameters need to be passed as keyword arguments i.e
    name=value
    '''
    
    @classmethod
    async def createKurento(cls):
        self = KurentoApi()
        return self

    async def ping(self):
        async with KurentoProtocol() as kurento:
            response = await kurento.request("ping")
            return response

    async def create(self,**kwargs):
        async with KurentoProtocol() as kurento:
            response = await kurento.request("create",**kwargs)
            return response

    async def invoke(self,**kwargs):
        async with KurentoProtocol() as kurento:
            response = await kurento.request("invoke",**kwargs)
            return response

    async def release(self,**kwargs):
        async with KurentoProtocol() as kurento: 
            response = await kurento.request("release",**kwargs)
            return response

    async def subscribe(self,**kwargs):
        async with KurentoProtocol() as kurento:
            response = await kurento.request("subscribe",**kwargs)
            return response

    async def unsubscribe(self,**kwargs):
        async with KurentoProtocol() as kurento:
            response = await kurento.request("unsubscribe",**kwargs)
            return response

    async def onevent(self,**kwargs):
        async with KurentoProtocol() as kurento:
            response = await kurento.request("onevent",**kwargs)
            return response

