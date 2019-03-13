from KApi import KurentoApi

class MediaPipeline(object):
    '''
    Class that helps in creating a Media Pipeline.
    Following the same factory pattern approach
    Need to store sessionId for further media Element creation
    '''

    @classmethod
    async def createMediaPipeline(self):
        self = MediaPipeline()
        self.api = await KurentoApi.createKurento()
        self.value = None
        self.sessionId = None
        return self

    async def create(self):
        response = await self.api.create(type='MediaPipeline',
                                         constructorParams={},
                                         properties={})
        if response.ok:
           self.value = response.result['value']
           self.sessionId = response.result['sessionId']
           return (self.value,self.sessionId)
        else:
           logging.error(response.message)
           return (None,None)

class WebRtcEndPoint(object):

    '''
    Class that invokes the basic methods for WebRtcEndpoint
    '''
    
    @classmethod
    async def createWebRtcEp(cls):
        self = WebRtcEndpoint()
        self.api = await KurentoApi.createKurento()
        self.mediaPipeline = None
        self.sessionId = None
        self.value = None
        return self

    async def create(self,mediaPipeline,sessionId):
        '''
        params: 
        mediaPipeline : value of pipeline to which this endpoint should belong
        sessionId : value of sessionId of the mediapipeline
        '''
       
        constParams = {"mediaPipline":mediaPipeline}
        response = await self.api.create(type = "WebRtcEndpoint",
                                        constructorParams = constParams,
                                        properties = {},
                                        sessionId = sessionId)
        if response.ok:
            self.sessionId = response.result['sessionId']
            self.value = response.result['value']
            return (self.value,self.sessionId)
        else:
            logging.error(response.message)
            return (None, None)
