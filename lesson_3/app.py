import asyncio
from typing import Optional
from loguru import logger

from web3.types import TxParams
from py_eth_async.data.models import Networks, TokenAmount, Unit, Ether
from py_eth_async.client import Client
from pretty_utils.miscellaneous.files import read_json
from py_eth_async.transactions import Tx

from tasks.woofi import WooFi
from tasks.woofi_universal import Woofi_universal
from data.models import Contracts
from data.config import ABIS_DIR
from private_data import private_key1, proxy
import sys


async def check_balance():
    client = Client(network=Networks.Ethereum, proxy=proxy, check_proxy=False)
    balance = await client.wallet.balance()
    print(f'balance: {balance.Ether} | {client.account.key.hex()} | {client.account.address}')
    if balance.Wei > 0:
        exit(1)


async def bruteforce(count_tasks: int):
    u1 = Unit(amount=1, unit='ether')
    u2 = Unit(amount=2, unit='ether')
    res = u1 * u2
    print(res.Ether)

    # while True:
    #     tasks = []
    #     for _ in range(count_tasks):
    #         tasks.append(asyncio.create_task(check_balance()))
    #     await asyncio.wait(tasks)


async def main():
    client = Client(private_key=private_key1, network=Networks.Arbitrum)

    # print(client.account.address)
    # print(await client.contracts.get_signature(hex_signature='0x7dc20382'))
    # print(await client.contracts.parse_function(text_signature='swap(address,address,uint256,uint256,address,address)'))
    # print(await client.contracts.get_contract_attributes(contract=Contracts.ARBITRUM_USDC))
    # print(await client.contracts.get_abi(contract_address=Contracts.ARBITRUM_USDC.address))

    # contract = await client.contracts.get(
    #     contract_address=Contracts.ARBITRUM_WOOFI.address,
    #     abi=read_json(path=(ABIS_DIR, 'woofi.json'))
    # )

    # print(await client.contracts.get_functions(contract=Contracts.ARBITRUM_USDC))

    # print((await client.wallet.balance()).Ether)
    # print(await client.wallet.nonce())

    # print((await client.transactions.gas_price(w3=client.w3)).Wei)
    # print(await client.transactions.max_priority_fee(w3=client.w3))

    # print(await client.transactions.decode_input_data(
    #     client=client,
    #     contract=Contracts.ARBITRUM_WOOFI,
    #     input_data='0x7dc20382000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000af88d065e77c8cc2239327c5edb3a432268e583100000000000000000000000000000000000000000000000000038d7ea4c6800000000000000000000000000000000000000000000000000000000000001be86500000000000000000000000069c1dc6d723f15d7ef8154ba7194977fcc90d85b00000000000000000000000069c1dc6d723f15d7ef8154ba7194977fcc90d85b'
    # ))

    #woofi = WooFi(client=client)
    # res = await woofi.swap_eth_to_usdc(amount=TokenAmount(amount=0.001))
    # res = await woofi.swap_usdc_to_eth()

    # Homework:
    # res = await woofi.swap_eth_to_usdt(amount=TokenAmount(amount=0.0005))     # tested - https://arbiscan.io/tx/0xf09e68ba61c8939be4b572642431bb2514e7bc18dbf260fd550a78283a19aa1e
    # res = await woofi.swap_usdt_to_eth()                                      # tested - https://arbiscan.io/tx/0x527dc11ed2b93a243cc387ae092c39ab7b9dbf50d50b6a41e26d8d48c62a53b6
    # res = await woofi.swap_eth_to_wbtc(amount=TokenAmount(amount=0.0005))     # tested - https://arbiscan.io/tx/0xb677fc9ebc2d6fb8c0c5ef525752f4f5d46ba42db3bea2de9fc8588a06f5a5c8
    # res = await woofi.swap_wbtc_to_eth()                                       # tested - https://arbiscan.io/tx/0x37159b6b12016da3e4580aeb3e72af7a61b05edea6d95e1862892df2010199cb

    # Homework2: Типо работает, но на самом деле так себе, сложности с получением цен на разные пары токенов,
    # надо делать как то уменее.

    universal_woofi = Woofi_universal(client=client)
    res = await universal_woofi.swap(client=client,
                                     amount=TokenAmount(amount=0.0001),
                                     token1=Contracts.ARBITRUM_ETH,
                                     token2=Contracts.ARBITRUM_USDC
                                     )
    if 'Failed' in res:
        logger.error(res)
    else:
        logger.success(res)

    #
    #
    #
    #
    #
    # #example of calling contract
    # contract = await client.contracts.default_token(contract_address=Contracts.ARBITRUM_USDT.address)
    # print(await contract.functions.symbol().call())
    #
    #

    # tx_hash = '0xf9bd50990974b8107a8ef1a2d2dc79c5de6114b42d5533827068ddccabe35240'
    # tx = Tx(tx_hash=tx_hash)
    # print(tx)
    # print(await tx.parse_params(client=client))
    # print(await tx.decode_input_data(client=client, contract=Contracts.ARBITRUM_WOOFI))


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
