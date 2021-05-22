#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 09:25:43 2021

@author: buseyarentekin
"""

from binance.client import Client


api_key="#custom_api_key"
api_secret="#custom_api_secret"

client=Client(api_key,api_secret)

price=0.00211111111111 #amount of price-changable
price=round(price,8)
quantity=5.111111111111  #amount of quantity-changable
quantity=round(quantity)

client.order_limit_buy(symbol="XRPETH", quantity=str(quantity),price=str(price),recvWindow=60000)
