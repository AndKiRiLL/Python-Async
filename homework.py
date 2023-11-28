# 1
'''
import asyncio, time

async def sum_1(a, b):
    print('Значения приняты')
    print('Идёт обработка ...')
    await asyncio.sleep(1)
    print(f'(sum_1) Результат: {a+b}')

async def sum_2(a):
    print('Значения получены')
    print('Идут подсчёты ...')
    await asyncio.sleep(2)
    print(f'(sum_2) Итог: {a**2}')

async def main():
    task1 = asyncio.create_task(sum_1(1,2))
    task2 = asyncio.create_task(sum_2(3))
    await asyncio.wait([task1, task2])

if __name__ == '__main__':
    asyncio.run(main())
'''

# 2 --------------------------------------------------------------------------------------------------------------------

import asyncio

async def phone():
    while True:
        print('Ожидание телефонного звонка...')
        await asyncio.sleep(1)

async def visitors():
    while True:
        print('Принимает поситителей...')
        await asyncio.sleep(2)

async def tickets():
    while True:
        print("Планирование билетов...")
        await asyncio.sleep(3)

async def schedules():
    while True:
        print("Работаем с расписание встреч...")
        await asyncio.sleep(4)

async def paperwork():
    while True:
        print('Работаем с документами...')
        await asyncio.sleep(5)

async def main():
    tasks = [
        phone(),
        visitors(),
        tickets(),
        schedules(),
        paperwork(),
    ]

    await asyncio.gather(*tasks)

asyncio.run(main())