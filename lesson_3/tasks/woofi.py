import asyncio
from typing import Optional
from web3.types import TxParams
from py_eth_async.data.models import TxArgs, TokenAmount

from data.models import Contracts
from tasks.base import Base


class WooFi(Base):
    async def swap_eth_to_usdc(self, amount: TokenAmount, slippage: float = 1):
        failed_text = 'Failed swap ETH to USDC via WooFi'

        contract = await self.client.contracts.get(contract_address=Contracts.ARBITRUM_WOOFI)
        from_token = Contracts.ARBITRUM_ETH
        to_token = Contracts.ARBITRUM_USDC

        eth_price = await self.get_token_price(token='ETH')
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
            return f'{amount.Ether} ETH was swaped to {min_to_amount.Ether} USDC via WooFi: https://arbiscan.io/tx/{tx.hash.hex()}'

        return f'{failed_text}!'

    async def swap_usdc_to_eth(self, amount: Optional[TokenAmount] = None, slippage: float = 1):
        failed_text = 'Failed swap USDC to ETH via WooFi'
        contract = await self.client.contracts.get(contract_address=Contracts.ARBITRUM_WOOFI)
        from_token = Contracts.ARBITRUM_USDC
        to_token = Contracts.ARBITRUM_ETH

        if not amount:
            amount = await self.client.wallet.balance(token=from_token)

        await self.approve_interface(token_address=from_token.address, spender=contract.address, amount=amount)
        await asyncio.sleep(5)

        eth_price = await self.get_token_price(token='ETH')
        min_to_amount = TokenAmount(
            amount=float(amount.Ether) / eth_price * (1 - slippage / 100)
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
            data=contract.encodeABI('swap', args=args.tuple())
        )

        tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
        receipt = await tx.wait_for_receipt(client=self.client, timeout=200)
        if receipt:
            return f'{amount.Ether} USDC was swaped to {min_to_amount.Ether} ETH via WooFi: https://arbiscan.io/tx/{tx.hash.hex()}'

        return f'{failed_text}!'

    async def swap_eth_to_usdt(self, amount: TokenAmount, slippage: float = 1):
        failed_text = 'Failed swap ETH to USDT via WooFi'

        contract = await self.client.contracts.get(contract_address=Contracts.ARBITRUM_WOOFI)
        from_token = Contracts.ARBITRUM_ETH
        to_token = Contracts.ARBITRUM_USDT

        eth_price = await self.get_token_price(token='ETH')
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
            return f'{amount.Ether} ETH was swaped to {min_to_amount.Ether} USDT via WooFi: https://arbiscan.io/tx/{tx.hash.hex()}'

        return f'{failed_text}!'


    async def swap_usdt_to_eth(self, amount: Optional[TokenAmount] = None, slippage: float = 1):
        failed_text = 'Failed swap USDT to ETH via WooFi'
        contract = await self.client.contracts.get(contract_address=Contracts.ARBITRUM_WOOFI)
        from_token = Contracts.ARBITRUM_USDT
        to_token = Contracts.ARBITRUM_ETH

        if not amount:
            amount = await self.client.wallet.balance(token=from_token)

        await self.approve_interface(token_address=from_token.address, spender=contract.address, amount=amount)
        await asyncio.sleep(5)

        eth_price = await self.get_token_price(token='ETH')
        min_to_amount = TokenAmount(
            amount=float(amount.Ether) / eth_price * (1 - slippage / 100)
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
            data=contract.encodeABI('swap', args=args.tuple())
        )

        tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
        receipt = await tx.wait_for_receipt(client=self.client, timeout=200)
        if receipt:
            return f'{amount.Ether} USDT was swaped to {min_to_amount.Ether} ETH via WooFi: https://arbiscan.io/tx/{tx.hash.hex()}'

        return f'{failed_text}!'



    async def swap_eth_to_wbtc(self, amount: TokenAmount, slippage: float = 1):
        failed_text = 'Failed swap ETH to WBTC via WooFi'

        contract = await self.client.contracts.get(contract_address=Contracts.ARBITRUM_WOOFI)
        from_token = Contracts.ARBITRUM_ETH
        to_token = Contracts.ARBITRUM_WBTC

        eth_price = await self.get_token_price(token1='ETH',token2='BTC')

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
            return (f'{amount.Ether} ETH was swaped to {min_to_amount.Ether} WBTC via WooFi: '
                    f'https://arbiscan.io/tx/{tx.hash.hex()}')

        return f'{failed_text}!'


    async def swap_wbtc_to_eth(self, amount: Optional[TokenAmount] = None, slippage: float = 1):
        failed_text = 'Failed swap WBTC to ETH via WooFi'
        contract = await self.client.contracts.get(contract_address=Contracts.ARBITRUM_WOOFI)
        from_token = Contracts.ARBITRUM_WBTC
        to_token = Contracts.ARBITRUM_ETH

        if not amount:
            amount = await self.client.wallet.balance(token=from_token)

        await self.approve_interface(token_address=from_token.address, spender=contract.address, amount=amount)
        await asyncio.sleep(5)


        eth_price = await self.get_token_price(token1='ETH',token2='BTC')
        print(eth_price)


        min_to_amount = TokenAmount(
            amount=float(amount.Ether) / eth_price * (1 - slippage / 100)
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
            data=contract.encodeABI('swap', args=args.tuple())
        )

        tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
        receipt = await tx.wait_for_receipt(client=self.client, timeout=200)
        if receipt:
            return (f'{amount.Ether} WBTC was swaped to {min_to_amount.Ether} ETH via WooFi: '
                    f'https://arbiscan.io/tx/{tx.hash.hex()}')

        return f'{failed_text}!'




    async def universsal_swap(self, amount: TokenAmount,
                            slippage: float = 1,
                            ticker1: str = "ETH",
                            ticker2: str = "USDC",
                            token1_contract: Contracts = Contracts.ARBITRUM_ETH,
                            token2_contract: Contracts = Contracts.ARBITRUM_USDC,
                            contract_address : Contracts = Contracts.ARBITRUM_WOOFI
                    ):
        print(type(amount))

        ticker1 = ticker1.upper() # token1_contract.ARBITRUM_USDC.symbol.call()
        ticker2 = ticker2.upper()
        failed_text = f'Failed swap {ticker1} to {ticker2} via WooFi'
        contract = await self.client.contracts.get(contract_address)
        from_token = token1_contract
        to_token = token2_contract



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
        eth_price = await self.get_token_price(token1=ticker1,token2=ticker_parse)

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

        if ticker1 != "ETH":
            tx_params = TxParams(
                to=contract.address,
                data=contract.encodeABI('swap', args=args.tuple()),
                value=amount.Wei
            )
        else:
            tx_params = TxParams(
                to=contract.address,
                data=contract.encodeABI('swap', args=args.tuple()),
                value=amount.Wei
            )


        tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
        receipt = await tx.wait_for_receipt(client=self.client, timeout=200)
        if receipt:
            return f'{amount.Ether} {ticker1} was swaped to {min_to_amount.Ether} {ticker2} via WooFi: https://arbiscan.io/tx/{tx.hash.hex()}' #

        return f'{failed_text}!'