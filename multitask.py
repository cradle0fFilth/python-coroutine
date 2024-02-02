import asyncio
import requests

async def request():
    url = 'http://baidu.com'
    status = requests.get(url)
    return status

def main():
    tasks = [asyncio.ensure_future(request()) for _ in range(5)]
    print("Task:",tasks)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    for task in tasks:
        print("Task result:",task.result())

if __name__=='__main__':
    main() 