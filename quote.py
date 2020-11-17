# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 23:46:39 2020

@author: 33667
"""

import requests
import urllib3
import json

URL = 'https://dolphin.jump-technology.com:8443/api/v1'
AUTH = ('EPITA_GROUPE3', 'X3fYKy2ehbgBdr4B')

class Quote:
    def __init__(self, close, coupon, date, gross, high, low, nav, ope, pl, ret, volume):
        self.close = close
        self.coupon = coupon  
        self.gross = gross
        self.high = high
        self.low = low 
        self.nav = nav
        self.ope = ope
        self.pl = pl
        self.ret = ret
        self.volume = volume
    
    def print_info(self):
        print("close " + str(self.close))
        print("coupon " + str(self.coupon))
        print("gross " + str(self.gross))
        print("high " + str(self.high))
        print("low " + str(self.low))
        print("nav " + str(self.nav))
        print("open " + str(self.ope))
        print("pl " + str(self.pl))
        print("return " + str(self.ret))
        print("close " + str(self.volume))
        

def get_assets(endpointApi, date=None, full_response=False):
    payload = {'date': date, 'fullResponse': full_response}
    res = requests.get(URL + endpointApi,
                       params=payload,
                       auth=AUTH,
                       verify=False)
    return res.content.decode('utf-8')

def get_quotes(endpointApi, data_id, quote, date=None, full_response=False):
    payload = {'id': int(data_id), 'start_quotes': "1985-04-12", 'end_quotes': "2020-11-17"}
    res = requests.get(URL + endpointApi + data_id + quote,
                       params=payload,
                       auth=AUTH,
                       verify=False)

    return res.content.decode('utf-8')
    
def asset_to_quotes(asset):
    obj_quotes = [] 
    result = get_quotes("/asset/", asset['ASSET_DATABASE_ID']['value'], "/quote")
    quotes = json.loads(result)

    for quote in quotes:
        close = quote.get('close', 'none')
        coupon = quote.get('coupon', 'none')
        date = quote.get('date', 'none')
        gross = quote.get('gross', 'none')
        high = quote.get('high', 'none')
        low = quote.get('low', 'none')
        nav = quote.get('nav', 'none')
        op = quote.get('open', 'none')
        pl = quote.get('pl', 'none')
        ret = quote.get('ret', 'none')
        volume = quote.get('volume', 'none')

        new_quote = Quote(close, coupon, date, gross, high, low, nav, op, pl, ret, volume)
        obj_quotes.append(new_quote)

    return obj_quotes

#------------ GET ASSETS --------------
actif = get_assets("/asset")
allActif = json.loads(actif)
#print("Mes actifs")
#print(actif)

#------------ GET QUOTES -------------
print("Mes quotes")
allQuotes = asset_to_quotes(allActif[1])

allQuotes[0].print_info()

#for elt in allQuotes:
#    elt.print_info()
   
#print("len of my quote list " + str(len(allQuotes)))
            
    