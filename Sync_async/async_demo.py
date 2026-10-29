from timeit import default_timer as timer
import asyncio


async def run_task(name, seconds):
    print(f'{name} started at: {timer()}')
    await asyncio.sleep(seconds)
    print(f'{name} completed at: {timer()}')



async def main():

    start = timer()
    await asyncio.gather(
        run_task('Task1', 2),
        run_task('Task2',1),
        run_task('Task3',3)
    )
    


    print(f'\n The total time taken : {timer() - start:.2f} s')



asyncio.run(main())