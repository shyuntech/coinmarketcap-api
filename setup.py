# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.0.2'

LONG_DESCRIPTION = """
=====================================
coinmarketcap-api (coinmarketcap-api)
=====================================
Python实现的 coinmarketcap.com APIs封装，同时提供了更多私有API实现
涵盖整体市场数据、虚拟货币数据、交易所数据等

Python wrapper for coinmarketcap.com public API and private API
offer global market data,coin data,exchanges data and more

Documentation
=============
https://github.com/shyuntech/coinmarketcap-api
"""

setup(
    name='coinmarketcap-api',
    version=version,
    description="Python wrapper for coinmarketcap.com public API and private API"
                "offer global market data,coin data,exchanges data and more",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['cryptocurrency', 'API', 'coinmarketcap'],
    author='hu chi',
    author_email='hu.chi@qq.com',
    url='https://github.com/shyuntech/coinmarketcap-api',
    license='Apache v2.0 License',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
