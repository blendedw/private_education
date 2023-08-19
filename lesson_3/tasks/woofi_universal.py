import asyncio
from typing import Optional
from web3.types import TxParams
from py_eth_async.data.models import TxArgs, TokenAmount
from py_eth_async.data.models import RawContract

from data.models import Contracts
from tasks.base import Base


class Woofi_universal(Base):
    async def swap(self,
                   client,
                   amount: TokenAmount,
                   slippage: float = 1,
                   contract_address: Contracts = Contracts.ARBITRUM_WOOFI,
                   token1: RawContract = None,
                   token2: RawContract = None,
                   ):
        if token1.address != Contracts.ARBITRUM_ETH.address:
            contract = await client.contracts.default_token(contract_address=token1.address)
            ticker1 = await contract.functions.symbol().call()
        else:
            ticker1 = "ETH"

        contract = await client.contracts.default_token(contract_address=token2.address)
        ticker2 = await contract.functions.symbol().call()

        failed_text = f'Failed swap {ticker1} to {ticker2} via WooFi'
        contract = await self.client.contracts.get(contract_address)
        from_token = token1
        to_token = token2

        if ticker1 != "ETH":
            print("Starting aprove")
            if not amount:
                amount = await self.client.wallet.balance(token=from_token)
            await self.approve_interface(token_address=from_token.address, spender=contract.address, amount=amount)
            await asyncio.sleep(5)

        if ticker2 == "WBTC":
            ticker_parse = "BTC"
        else:
            ticker_parse = ticker2
        eth_price = await self.get_token_price(token1=ticker1, token2=ticker_parse)

        min_to_amount = TokenAmount(
            amount=eth_price * float(amount.Ether) * (1 - slippage / 100),
            decimals=await self.get_decimals(contract_address=to_token.address)
        )

        args = TxArgs(
            fromToken=from_token.address,
            toToken=to_token.address,
            fromAmount=amount.Wei,
            minToAmount=min_to_amount.Wei,
            to=self.client.account.address,
            rebateTo=self.client.account.address,
        )

        tx_params = TxParams(
            to=contract.address,
            data=contract.encodeABI('swap', args=args.tuple()),
            value=amount.Wei
        )

        tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
        receipt = await tx.wait_for_receipt(client=self.client, timeout=200)
        if receipt:
            return f'{amount.Ether} {ticker1} was swaped to {min_to_amount.Ether} {ticker2} via WooFi: https://arbiscan.io/tx/{tx.hash.hex()}'  #

        return f'{failed_text}!'
