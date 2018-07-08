#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tempfile
import json
import os
import requests
import requests_cache


class ApiClient(object):
    """
    coinmarketcap.com api wrapper with request cache feature
    """
    _session = None

    def __init__(self, request_timeout, enable_cache,
                 cache_filename, cache_expire_after):
        self.request_timeout = request_timeout
        self.enable_cache = enable_cache
        self.cache_filename = cache_filename
        self.cache_expire_after = cache_expire_after
        self.cache_file = os.path.join(tempfile.gettempdir(), self.cache_filename) if enable_cache else None

    @property
    def session(self):
        """
        wrapper for _session
        :return: 
        """
        if self._session is None:
            if self.enable_cache:
                requests_cache.install_cache(self.cache_file, backend='sqlite', expire_after=self.cache_expire_after)
            self._session = requests.Session()
            self._session.headers.update({'Content-Type': 'application/json'})
            self._session.headers.update(
                {'User-agent': 'coinmarketcap-api(https://github.com/shyuntech/coinmarketcap-api)'})
        return self._session

    def request(self, base_url, endpoint, params, disable_cache=False):
        print(base_url + endpoint)
        if disable_cache:
            with requests_cache.disabled():
                resp = self.session.get(base_url + endpoint, params=params, timeout=self.request_timeout)
        else:
            resp = self.session.get(base_url + endpoint, params=params, timeout=self.request_timeout)
        try:
            resp_json = json.loads(resp.text)
            if isinstance(resp_json, dict) and resp.status_code == 200:
                resp_json[u'cached'] = disable_cache
        except Exception as e:
            return e
        return resp_json

    def raw_request(self, base_url, endpoint, params, disable_cache=False):
        if disable_cache:
            disable_cache_session = self.session
            with requests_cache.disabled():
                resp = disable_cache_session.get(base_url + endpoint, params=params, timeout=self.request_timeout)
        else:
            resp = self.session.get(base_url + endpoint, params=params, timeout=self.request_timeout)

        return resp.text
