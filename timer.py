import asyncio
import time
 
async def block(seconds):
    start = time.time()
    await asyncio.sleep(seconds)
    elapsed = time.time() - start
    print('blocked since', elapsed)
 
async def main():
    t1 = asyncio.create_task(block(1))
    t2 = asyncio.create_task(block(2))
    start = time.time()
    z = await asyncio.gather(t1, t2)
    print('elapsed: ', time.time() - start)
    return z
 
asyncio.run(main())