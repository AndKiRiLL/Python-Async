import asyncio
# ----------------------------------------------------------------------------------------------------------------------
'''
async def async_func():
    print('Запуск ...')
    await asyncio.sleep(1)
    print('... Готово!')

async def main():
    async_func()
    await async_func()

asyncio.run(main())
'''
# ----------------------------------------------------------------------------------------------------------------------
'''
async def async_func():
    print('Запуск ...')
    await asyncio.sleep(1)
    print('... Готово!')

async def main():
    task = asyncio.create_task(async_func())
    await task

asyncio.run(main())
'''
# ----------------------------------------------------------------------------------------------------------------------
'''
async def async_func(task_no):
    print(f'{task_no}: Запуск ...')
    await asyncio.sleep(1)
    print(f'{task_no}: ... Готово!')

async def main():
    taskA = asyncio.create_task(async_func('taskA'))
    taskB = asyncio.create_task(async_func('taskB'))
    taskC = asyncio.create_task(async_func('taskC'))
    await asyncio.wait([taskA, taskB, taskC])

if __name__ == '__main__':
    asyncio.run(main())
'''
# ----------------------------------------------------------------------------------------------------------------------
'''
async def async_function(a):
    while True:
        await a
        a = a + 1
'''
# ----------------------------------------------------------------------------------------------------------------------
'''
async def count(counter):
    print(f"Количество записей в списке {len(counter)}")
    while True:
        await asyncio.sleep(1 / 1000)
        counter.append(1)

async def print_every_sec(counter):
    while True:
        await asyncio.sleep(1)
        print(f'- 1 секунда прошла. '
              f'Количество записей в списке: {len(counter)}')

async def print_every_5_sec():
    while True:
        await asyncio.sleep(5)
        print(f'---- 5 секунд прошло')

async def print_every_10_sec():
    while True:
        await asyncio.sleep(10)
        print(f'---------- 10 секунд прошло')

# 1.
async def main():
    counter = list()
    tasks = [
        # 2.
        count(counter),
        print_every_sec(counter),
        print_every_5_sec(),
        print_every_10_sec()
    ]
    # 3, 4.
    await asyncio.gather(*tasks)

# 5.
asyncio.run(main())
'''
# ----------------------------------------------------------------------------------------------------------------------
'''
import time

async def brewCoffee():
    print("Start brewCoffee()")
    await asyncio.sleep(3)
    print("End brewCoffee()")
    return "Coffee ready"

async def toastBage1():
    print("Start toastBage1()")
    await asyncio.sleep(2)
    print("End toastBage1()")
    return "Bage1 toasted"

async def main():
    start_time = time.time()

    # batch = asyncio.gather(brewCoffee(), toastBage1())
    # result_coffee, result_bage1 = await batch

    coffee_task = asyncio.create_task(brewCoffee())
    toast_task = asyncio.create_task(toastBage1())

    result_coffee = await coffee_task
    result_bage1 = await toast_task

    end_time = time.time()
    spent_time = end_time - start_time
    print(f'Result of brewCoffe: {result_coffee}')
    print(f'Result of toastBage1: {result_bage1}')
    print(f'Total execution time: {spent_time:.2f} seconds')

if __name__ == '__main__':
    asyncio.run(main())
'''
# ----------------------------------------------------------------------------------------------------------------------
'''
async def my_sleep():
    print('my sleep start')
    await asyncio.sleep(2)
    print('my sleep end')

async def main():
    print('sleep now')
    await my_sleep()
    print('Ok. Wake up')

if __name__ == "__main__":
    asyncio.run(main())
'''
# ----------------------------------------------------------------------------------------------------------------------
import httpx

async def download(current_page):
    url = f'https://catfact.ninja/fact'

    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        if r.status_code == 200:
            _r = r.json()
            print(_r.get('fact'))
        else:
            print(r.status_code)
    print(f' {current_page}')

async def main():
    page_count = int(input("Page count? "))

    current_page = 0
    task_list = []
    while current_page < page_count:
        current_page += 1
        task = asyncio.create_task(download(current_page))
        task_list.append(task)
        # await download(current_page)
    await asyncio.gather(*task_list, return_exceptions=True)
    print('Done')

asyncio.run(main())
