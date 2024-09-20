import asyncio


async def start_strongman(name, power):

    print(f'Силач {name} начал соревнования.')
    ball_number = 1
    for i in range(5):
        await asyncio.sleep(24/power)
        print(f'Силач {name} поднял {ball_number} шар')
        ball_number += 1
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():

    task_1 = asyncio.create_task(start_strongman('Arnold', 12))
    task_2 = asyncio.create_task(start_strongman('Silvestr', 16))
    task_3 = asyncio.create_task(start_strongman('Fedor', 24))
    await task_1
    await task_2
    await task_3

asyncio.run(start_tournament())
