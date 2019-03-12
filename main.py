import asyncio
from KElements import MediaPipeline

async def main():
    mediaPipe = await MediaPipeline.createMediaPipeline()
    (value,sessionId) = await mediaPipe.create()
    print("SessionId : {}".format(sessionId))

if __name__=="__main__":
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(main())
    
