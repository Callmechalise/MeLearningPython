#asyncIO
import asyncio
async def f1(n):
    print (n*n*n)
    await asyncio.sleep(10)
async def f2(n):
    print (n*n)
    await asyncio.sleep(10)
async def f3(n):
    print (n)
    await asyncio.sleep(10)
async def main():
    l= await asyncio.gather(
        f1(5),
        f2(5),
        f3(5)
    )
    print(l)
asyncio.run(main())
#overall ma parallely run garxa fast execute garxa
