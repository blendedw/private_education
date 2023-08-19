from pretty_utils.type_functions.classes import Singleton
from py_eth_async.data.models import RawContract, DefaultABIs
from pretty_utils.miscellaneous.files import read_json

from data.config import ABIS_DIR


class Contracts(Singleton):
    ARBITRUM_WOOFI = RawContract(
        address='0x9aed3a8896a85fe9a8cac52c9b402d092b629a30', abi=read_json(path=(ABIS_DIR, 'woofi.json'))
    )

    ARBITRUM_USDC = RawContract(
        address='0xaf88d065e77c8cC2239327C5EDb3A432268e5831', abi=DefaultABIs.Token
    )

    ARBITRUM_ETH = RawContract(
        address='0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE', abi=DefaultABIs.Token
    )

    ARBITRUM_USDT = RawContract( #https://arbiscan.io//tx/0x0ff210f01799eeb113fcfbd7e956dd03752f6c25d3d934803f67da6d04daa658
        address='0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9', abi=DefaultABIs.Token
    )

    ARBITRUM_WBTC = RawContract( #https://arbiscan.io//tx/0x0cbe3c825f5c0292afd0e111e5f85f82202dcd0f4513e1f11f5f03c838234a9b
        address='0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f', abi=DefaultABIs.Token
    )

