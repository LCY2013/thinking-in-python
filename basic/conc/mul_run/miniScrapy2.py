import asyncio


# @coroutine是 的功能类似物，async def但它可以在 Python 3.4+ 中工作，并使用yield from构造而不是await.
# @asyncio.coroutine
# def task():
#     print('request')
#     yield from asyncio.sleep(3)
#     print('response')


# async def是 Python 3.5 的新语法。您可以在函数内使用await,async with和。async for async def
async def task():
    print('request')
    await asyncio.sleep(3)
    print('response')


scheduler = [task(), task(), task()]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*scheduler))
loop.close()
