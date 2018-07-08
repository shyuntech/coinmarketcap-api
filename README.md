# coinmarketcap-api


####intro

Python wrapper for coinmarketcap.com public API and private API
offer global market data,coin data,exchanges data and more
this library has been tested with Python2.7 and Python3.6

##Install

From source use

    $ python setup.py install

or install from PyPi

    $ pip install coinmarketcap-api
    
##Usage

#### 1. global market state
- **`Implement`** - Use coinmarketcap.com public API /v2/global/
- **`Description`** - This endpoint displays the global data found at the top of coinmarketcap.com.
- **`Optional parameters:`**
    - **(string) convert** - return pricing info in terms of another currency.
    Valid fiat currency values are: “AUD”, “BRL”, “CAD”, “CHF”, “CLP”, “CNY”, “CZK”, “DKK”, “EUR”, “GBP”, “HKD”, “HUF”, “IDR”, “ILS”, “INR”, “JPY”, “KRW”, “MXN”, “MYR”, “NOK”, “NZD”, “PHP”, “PKR”, “PLN”, “RUB”, “SEK”, “SGD”, “THB”, “TRY”, “TWD”, “ZAR”
    Valid cryptocurrency values are: “BTC”, “ETH” “XRP”, “LTC”, and “BCH”

#####example
```python
from coinmarketcap import CoinMarketCap
market = CoinMarketCap()
resp = market.stats(convert="BTC")
{
	'data': {
		'active_cryptocurrencies': 1620,
		'active_markets': 11598,
		'bitcoin_percentage_of_market_cap': 42.11,
		'quotes': {
			'USD': {
				'total_market_cap': 277757148004.0,
				'total_volume_24h': 12371915084.0
			},
			'BTC': {
				'total_market_cap': 40697435.0,
				'total_volume_24h': 1812753.0
			}
		},
		'last_updated': 1531038676
	},
	'metadata': {
		'timestamp': 1531038328,
		'error': None
	},
	'cached': False
}
```

#### 2. coins list
- **`Implement`** - Use coinmarketcap.com public API /v2/listings/
- **`Description`** - This endpoint displays all active cryptocurrency listings in one call. Use the "id" field on 
        the Ticker endpoint to query more information on a specific cryptocurrency.

#####example
```python
from coinmarketcap import CoinMarketCap
market = CoinMarketCap()
resp = market.coin_list()
{
	'data': [{
		'id': 1,
		'name': 'Bitcoin',
		'symbol': 'BTC',
		'website_slug': 'bitcoin'
	}, {
		'id': 2,
		'name': 'Litecoin',
		'symbol': 'LTC',
		'website_slug': 'litecoin'
	}//...
	],
	'metadata': {
		'timestamp': 1531038439,
		'num_cryptocurrencies': 1620,
		'error': None
	},
	'cached': False
}
```

#### 3. coins ticker detail
- **`Implement`** - Use coinmarketcap.com public API /v2/ticker/`coinid`/
- **`Description`** - This endpoint displays cryptocurrency ticker data in order of rank. The maximum 
        number of results per call is 100. Pagination is possible by using the start 
        and limit parameters.
- **`Optional parameters:`**
    - **(int) start** - return results starting from the specified number (default is 1)
    - **(int) limit** - return a maximum of [limit] results (default is 100; max is 100)
    - **(string) sort** - return results sorted by [sort] . Possible values are id, rank, volume_24h, and 
    percent_change_24h (default is rank). 
    Note: It is strongly recommended to use id to sort if paginating through all available results since id is the only sort option guaranteed to return in a consistent order.
    - **(string) structure** - specify the structure for the main data field. Possible values are dictionary and array (default is dictionary).
    - **(string) convert** - return pricing info in terms of another currency. 
    Valid fiat currency values are: "AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR" 
    Valid cryptocurrency values are: "BTC", "ETH" "XRP", "LTC", and "BCH"

#####example
```python
from coinmarketcap import CoinMarketCap
market = CoinMarketCap()
resp = market.coin_ticker_detail(1, convert="CNY", disable_cache=False)
{
	'data': {
		'id': 1,
		'name': 'Bitcoin',
		'symbol': 'BTC',
		'website_slug': 'bitcoin',
		'rank': 1,
		'circulating_supply': 17137487.0,
		'total_supply': 17137487.0,
		'max_supply': 21000000.0,
		'quotes': {
			'USD': {
				'price': 6826.71,
				'volume_24h': 3921270000.0,
				'market_cap': 116992653878.0,
				'percent_change_1h': -0.05,
				'percent_change_24h': 2.75,
				'percent_change_7d': 7.06
			},
			'CNY': {
				'price': 45340.3158747659,
				'volume_24h': 26043529083.591248,
				'market_cap': 777019073880.0,
				'percent_change_1h': -0.05,
				'percent_change_24h': 2.75,
				'percent_change_7d': 7.06
			}
		},
		'last_updated': 1531038856
	},
	'metadata': {
		'timestamp': 1531038527,
		'error': None
	},
	'cached': False
}
```

#### 4. coins ticker list
- **`Implement`** - Use coinmarketcap.com public API /v2/ticker/
- **`Description`** - This endpoint displays cryptocurrency ticker data in order of rank. The maximum 
        number of results per call is 100. Pagination is possible by using the start 
        and limit parameters.
- **`Optional parameters:`**
    - **(int) start** - return results starting from the specified number (default is 1)
    - **(int) limit** - return a maximum of [limit] results (default is 100; max is 100)
    - **(string) sort** - return results sorted by [sort] . Possible values are id, rank, volume_24h, and 
    percent_change_24h (default is rank). 
    Note: It is strongly recommended to use id to sort if paginating through all available results since id is the only sort option guaranteed to return in a consistent order.
    - **(string) structure** - specify the structure for the main data field. Possible values are dictionary and array (default is dictionary).
    - **(string) convert** - return pricing info in terms of another currency. 
    Valid fiat currency values are: "AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR" 
    Valid cryptocurrency values are: "BTC", "ETH" "XRP", "LTC", and "BCH"

#####example
```python
from coinmarketcap import CoinMarketCap
market = CoinMarketCap()
resp = market.coin_ticker_list(convert="CNY", start=1, limit=2, disable_cache=False)
{
	'data': {
		'1': {
			'id': 1,
			'name': 'Bitcoin',
			'symbol': 'BTC',
			'website_slug': 'bitcoin',
			'rank': 1,
			'circulating_supply': 17137562.0,
			'total_supply': 17137562.0,
			'max_supply': 21000000.0,
			'quotes': {
				'USD': {
					'price': 6819.96,
					'volume_24h': 3918890000.0,
					'market_cap': 116877487338.0,
					'percent_change_1h': -0.18,
					'percent_change_24h': 2.64,
					'percent_change_7d': 6.98
				},
				'CNY': {
					'price': 45295.4850364624,
					'volume_24h': 26027722062.085728,
					'market_cap': 776254183132.0,
					'percent_change_1h': -0.18,
					'percent_change_24h': 2.64,
					'percent_change_7d': 6.98
				}
			},
			'last_updated': 1531041083
		},
		'1027': {
			'id': 1027,
			'name': 'Ethereum',
			'symbol': 'ETH',
			'website_slug': 'ethereum',
			'rank': 2,
			'circulating_supply': 100558036.0,
			'total_supply': 100558036.0,
			'max_supply': None,
			'quotes': {
				'USD': {
					'price': 492.025,
					'volume_24h': 1402710000.0,
					'market_cap': 49477067647.0,
					'percent_change_1h': -0.18,
					'percent_change_24h': 4.15,
					'percent_change_7d': 8.44
				},
				'CNY': {
					'price': 3267.8360320391,
					'volume_24h': 9316246695.801176,
					'market_cap': 328607173247.0,
					'percent_change_1h': -0.18,
					'percent_change_24h': 4.15,
					'percent_change_7d': 8.44
				}
			},
			'last_updated': 1531041074
		}
	},
	'metadata': {
		'timestamp': 1531040731,
		'num_cryptocurrencies': 1620,
		'error': None
	},
	'cached': False
}
```


#### 5. coins price
- **`Implement`** - Use coinmarketcap.com private API https://graphs2.coinmarketcap.com/currencies/`currency`/`start`/`end`/
- **`Description`** - This endpoint get currency price info from `start` to `end`.
- **`Optional parameters:`**
    - **(int) start** - return results starting from the specified timestamp
    - **(int) end** - return results ending with the specified timestamp
    Note: You should set start and end both or both not
    
#####example
```python
from coinmarketcap import CoinMarketCap
market = CoinMarketCap()
resp = market.coin_price("eos")
{
	'market_cap_by_available_supply': [
		[1498936454000, 0],
		[1499022857000, 0],
		//more data here
	],
	'price_platform': [
		[1498936454000, 0.00379662],
		[1499022857000, 0.008883],
		//more data here
	],
	'price_usd': [
		[1498936454000, 1.03134],
		[1499022857000, 2.51268],
		//more data here
	],
	'volume_usd': [
		[1498936454000, 11487600],
		[1499022857000, 288045000],
		//more data here
	],
	'cached': False
}
```


#### 6. coins market price
- **`Implement`** - gather coin market price from web page https://coinmarketcap.com/currencies/`currency`/#markets
- **`Description`** - This endpoint return currency market price info 

#####example
```python
from coinmarketcap import CoinMarketCap
market = CoinMarketCap()
resp = market.coin_market_price("eos")
{
	'data': [{
		'exchange': 'OKEx',
		'pair': 'EOS/USDT',
		'volume': {
			'volume_usd': '78479600.0',
			'volume_btc': '11670.3',
			'volume_native': '8586700.0'
		},
		'price': {
			'price_usd': '9.13968',
			'price_btc': '0.00135911',
			'price_native': '8.8138'
		},
		'percentage': '14.6980406258'
	}, {
		'exchange': 'CoinBene',
		'pair': 'EOS/USDT',
		'volume': {
			'volume_usd': '68980700.0',
			'volume_btc': '10257.8',
			'volume_native': '7550640.0'
		},
		'price': {
			'price_usd': '9.13573',
			'price_btc': '0.00135853',
			'price_native': '8.81'
		},
		'percentage': '12.9190405022'
	}],
	'metadata': {
		'num_prices': 124,
		'error': None
	}
}
```

#### 6. exchange list
- **`Implement`** - gather exchanges list from web page https://coinmarketcap.com/exchanges/volume/24-hour/all/
- **`Description`** - This endpoint displays all active exchange listings in one call. 
#####example
```python
from coinmarketcap import CoinMarketCap
market = CoinMarketCap()
resp = market.exchange_list()
{
	'data': [{
		'display_name': 'FCoin',
		'name': 'fcoin',
		'url': '/exchanges/fcoin/',
		'logo': 'https://s2.coinmarketcap.com/static/img/exchanges/32x32/410.png',
		'rank': 1
	}, {
		'display_name': 'BitMEX',
		'name': 'bitmex',
		'url': '/exchanges/bitmex/',
		'logo': 'https://s2.coinmarketcap.com/static/img/exchanges/32x32/157.png',
		'rank': 2
	}],
	'metadata': {
		'num_exchanges': 207,
		'error': None
	}
}
```

#### 7. exchange detail
TODO