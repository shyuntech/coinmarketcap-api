#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def get_name_form_url(url):
    return re.match(r'/exchanges/(.*)/', url).group(1)


def get_price(td):
    try:
        price_span = td.find(u"span", {u"class": u"price"})
        price = {
            u'price_usd': price_span[u"data-usd"],
            u'price_btc': price_span[u"data-btc"],
            u'price_native': price_span[u'data-native'],
        }
        return price
    except Exception as error:
        return None


def get_volume(td):
    try:
        price_span = td.find(u"span", {u'class': u'volume'})
        volume = {
            u'volume_usd': price_span[u'data-usd'],
            u'volume_btc': price_span[u'data-btc'],
            u'volume_native': price_span[u'data-native'],
        }
        return volume
    except Exception as error:
        return None
