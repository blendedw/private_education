import asyncio

from web3 import Web3

from sdk.data.models import Networks
from sdk.client import Client

from private_data import private_key1, proxy #private_key2, private_key3,
from loguru import logger

async def check_wallet():
    client = Client(network=Networks.Arbitrum, proxy=proxy)
    balance = await client.wallet.balance()

    while balance == 0:
        client = Client(network=Networks.Arbitrum, proxy=proxy)
        balance = await client.wallet.balance()
        logger.info(f'trying {client.account.address} has balance of {balance}')
        await asyncio.sleep(1) # что бы прокси не устали
    logger.info(f"FOUND BALANCE {client.account.address} has balance of {balance} and here is it's private key {client.account.key}")


    return balance




async def main(count):
    tasks = []
    for i in range(count):
        tasks.append(asyncio.create_task(check_wallet()))
    await asyncio.wait(tasks)



if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main(10))

















    '''
    token_address = Web3.to_checksum_address('0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8')

    tasks = []
    for private_key in [private_key1, private_key2, private_key3]:
        client = Client(private_key=private_key, network=Networks.Arbitrum)
        tasks.append(asyncio.create_task(client.wallet.balance(token_address=token_address)))

    await asyncio.gather(*tasks)
    await asyncio.wait([*tasks])

    for task in tasks:
        print(task.result())
    '''
    '''
    asyncio.gather() принимает список асинхронных задач (coroutines) в качестве аргументов и запускает их одновременно.
    Она возвращает список результатов, соответствующих выполненным задачам в том же порядке, в котором задачи были переданы в функцию.
    Если во время выполнения задачи возникает исключение, asyncio.gather() прекращает выполнение остальных задач и сразу же выбрасывает исключение.

    asyncio.wait() принимает список асинхронных задач (coroutines) в качестве аргументов и запускает их одновременно.
    Она возвращает кортеж из двух множеств: множество выполненных задач и множество невыполненных задач.
    Если во время выполнения задачи возникает исключение, asyncio.wait() продолжает выполнение остальных задач и не выбрасывает исключение.
    '''


