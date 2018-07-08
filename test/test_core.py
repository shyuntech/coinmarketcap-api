import unittest
from coinmarketcap import CoinMarketCap


class TestCoinMarketCap(unittest.TestCase):
    """
    unit test case for CoinMarketCap lib
    """
    market = None

    def setUp(self):
        self.market = CoinMarketCap()
        super(TestCoinMarketCap, self).setUp()

    def test_stats(self):
        market = CoinMarketCap()
        resp = market.stats(convert="BTC")
        print(resp)
        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp['data']['quotes']['BTC'])
        self.assertIsNone(resp['metadata']['error'])
        #

    def test_coin_list(self):
        resp = self.market.coin_list()
        print(resp)
        self.assertIsNotNone(resp)

    def test_coin_ticker_detail(self):
        market = CoinMarketCap()
        resp = market.coin_ticker_detail(1, convert="CNY", disable_cache=False)
        print(resp)
        self.assertIsNotNone(resp)

    def test_coin_ticker_list(self):
        market = CoinMarketCap()
        resp = market.coin_ticker_list(convert="CNY", start=1, limit=2, disable_cache=False)
        print(resp)
        self.assertIsNotNone(resp)

    def test_price(self):
        market = CoinMarketCap()
        resp = market.coin_price("eos")
        print(resp)
        self.assertIsNotNone(resp)

    def test_market_price(self):
        market = CoinMarketCap()
        resp = market.coin_market_price("eos")
        print(resp)
        self.assertIsNotNone(resp)

    def test_exchange_list(self):
        market = CoinMarketCap()
        resp = market.exchange_list()
        print(resp)
        self.assertIsNotNone(resp)

    def test_exchange_detail(self):
        market = CoinMarketCap()
        resp = market.exchange_detail()
        print(resp)
        self.assertIsNotNone(resp)
