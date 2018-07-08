#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from coinmarketcap import utils

from bs4 import BeautifulSoup as bs
from coinmarketcap.client import ApiClient


class CoinMarketCap(object):
    """
    
    market = CoinMarketCap()
    market.coin_list()
    """
    __CMC_API_URL = u'https://api.coinmarketcap.com/v2/'
    __CMC_HISTORY_API_URL = u'https://graphs2.coinmarketcap.com/'
    __CMC_BASE_URL = u'https://coinmarketcap.com/'
    __DEFAULT_REQUEST_TIMEOUT = 60  # seconds
    __DEFAULT_ENABLE_CACHE = True
    __DEFAULT_CACHE_FILENAME = u'coinmarketcap.cache'
    __DEFAULT_CACHE_EXPIRE_AFTER = 60  # seconds

    def __init__(self, enable_cache=__DEFAULT_ENABLE_CACHE, request_timeout=__DEFAULT_REQUEST_TIMEOUT,
                 cache_expire_after=__DEFAULT_CACHE_EXPIRE_AFTER, cache_filename=__DEFAULT_CACHE_FILENAME):
        self.client = ApiClient(request_timeout, enable_cache, cache_filename, cache_expire_after)

    def stats(self, **kwargs):
        """
        This endpoint displays the global data found at the top of coinmarketcap.com.

        Optional parameters:
        (string) convert - return pricing info in terms of another currency.
        Valid fiat currency values are: "AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK",
        "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN",
        "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY",
        "TWD", "ZAR"
        Valid cryptocurrency values are: "BTC", "ETH" "XRP", "LTC", and "BCH"
        """

        params = {}
        params.update(kwargs)
        response = self.client.request(self.__CMC_API_URL, u'global/', params)
        return response

    def coin_list(self, disable_cache=False):
        """
        This endpoint displays all active cryptocurrency listings in one call. Use the "id" field on 
        the Ticker endpoint to query more information on a specific cryptocurrency.
        
        GET /listings/
        
        :param disable_cache:  是否启用缓存
        :return: json
        """
        response = self.client.request(self.__CMC_API_URL, u'listings/', params=None, disable_cache=disable_cache)
        return response

    def coin_ticker_list(self, disable_cache=False, **kwargs):
        print(kwargs)
        print(disable_cache)
        return self.coin_ticker_detail(currency="", disable_cache=disable_cache, **kwargs)

    def coin_ticker_detail(self, currency, disable_cache=False, **kwargs):
        """
        This endpoint displays cryptocurrency ticker data in order of rank. The maximum 
        number of results per call is 100. Pagination is possible by using the start 
        and limit parameters.
        
        GET /ticker/
        GET /ticker/<coin id>
        
        Optional parameters:
            (int) start - return results starting from the specified number (default is 1)
            (int) limit - return a maximum of [limit] results (default is 100; max is 100)
            (string) sort - return results sorted by [sort] . Possible values are id, rank, volume_24h, and 
            percent_change_24h (default is rank). 
            Note: It is strongly recommended to use id to sort if paginating through all available results since id is the only sort option guaranteed to return in a consistent order.
            (string) structure - specify the structure for the main data field. Possible values are dictionary and array (default is dictionary).
            (string) convert - return pricing info in terms of another currency. 
            Valid fiat currency values are: "AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR" 
            Valid cryptocurrency values are: "BTC", "ETH" "XRP", "LTC", and "BCH"

        :param currency: 货币
        :param disable_cache: 
        :return: 
        """
        params = {}
        params.update(kwargs)
        # see https://github.com/barnumbirr/coinmarketcap/pull/28
        if currency:
            currency = str(currency) + u'/'

        response = self.client.request(self.__CMC_API_URL, u'ticker/' + currency, params, disable_cache)
        return response

    def coin_price(self, currency, start=None, end=None, disable_cache=False):
        """
        get currency price info from <start> to <end>
        
        GET /currencies/<currency>/<start>/<end>/
        GET /currencies/<currency>/
        
        Optional parameters:
            (int) start - return results starting from the specified timestamp
            (int) end - return results ending with the specified timestamp
            
        :param currency: 货币名称 必须是字符串
        :param disable_cache: 禁用缓存
        :param start: 开始时间timestamp
        :param end: 结束时间timestamp
        :return: 
        """
        if all((start, end)):
            endpoint = u'currencies/{}/{}/{}'.format(currency, start, end)
        else:
            endpoint = u'currencies/{}/'.format(currency)
        response = self.client.request(self.__CMC_HISTORY_API_URL, endpoint, None, disable_cache)

        return response

    def coin_market_price(self, currency, disable_cache=False):
        """
        https://coinmarketcap.com/currencies/<currency>/#markets
        
        :param currency: 虚拟货币的名称 eg：bitcoin
        :param disable_cache: 禁用缓存默认为
        :return: 
        """
        endpoint = u'currencies/{}/#markets'.format(currency)
        response = self.client.raw_request(self.__CMC_BASE_URL, endpoint, None, disable_cache)

        soup = bs(response, u'html.parser')
        table_body = soup.find(u'table', {u'id': u'markets-table'}).find(u'tbody')
        rows = table_body.find_all(u'tr')
        items = []
        for row in rows:
            tds = row.find_all(u'td')
            item = {
                u'exchange': tds[1][u'data-sort'],
                u'pair': tds[2][u'data-sort'],
                u'volume': utils.get_volume(tds[3]),
                u'price': utils.get_price(tds[4]),
                u'percentage': tds[5][u'data-sort']
            }
            items.append(item)
        resp = {
            u'data': items,
            u"metadata": {
                u"num_prices": len(items),
                u"error": None
            }
        }
        return resp

    def exchange_list(self, disable_cache=False):
        """
        https://coinmarketcap.com/exchanges/volume/24-hour/all/ 
        This endpoint displays all active exchange listings in one call. 
        
        GET /exchanges/volume/24-hour/all/
        
        :param disable_cache:  禁用缓存
        :return: 
        """
        endpoint = u'exchanges/volume/24-hour/all/'
        response = self.client.raw_request(self.__CMC_BASE_URL, endpoint, None, disable_cache)
        soup = bs(response, u'html.parser')

        rows = soup.find_all(u'h3', {u'class': u'padding-top--lv6 margin-bottom--lv2'})
        items = []
        for idx, row in enumerate(rows, start=1):
            item = {
                u'display_name': row.find(u'a', {u'class': u'link-secondary'}).get_text(),
                u'name': utils.get_name_form_url(row.find(u'a', {u'class': u'link-secondary'})[u'href']),
                u'url': row.find(u'a', {u'class': u'link-secondary'})[u'href'],
                u'logo': row.find(u'img', {u'class': u'logo-32x32'})[u'src'],
                u'rank': idx,
            }
            items.append(item)
        resp = {
            u'data': items,
            u"metadata": {
                u"num_exchanges": len(items),
                u"error": None
            }
        }
        return resp

    def exchange_detail(self):
        # TODO gather exchange info from webpage
        pass
