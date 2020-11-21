import json

from models.dynAmountLineAsset import DynAmountLineAsset
from apiTools import get_portfolio
from models.portfolio import jsonToPortfolio
from models.quote import asset_to_quotes
from vars import *
"""
def enough_assets(portfolio):
    count = 0
    for elt in portfolio:
        if elt['asset']:
            count += float(elt['asset']['quantity'])
        
    return count > 15 and count < 40
"""

def enough_assets(portfolio):
    count = 0
    for elt in portfolio.values["2016-06-01"]:
        if elt.asset:
            count += elt.asset.quantity
            
    if count > 15 and count < 40:
        print("La quantité d'action pour ce portfolio est correcte")
        return True
    print("La quantité d'action pour ce portfolio n'est PAS correcte")
    return False


def is_uniq_compo(portfolio):
    if portfolio.values["2016-06-01"]:
        print("Ce portefeuille est une composition unique du 2016-06-01")
        return True
    print("Ce portefeuille n'est PAS une composition unique du 2016-06-01")
    return False


def check_nav(port_ID):
   str_port = get_portfolio(port_ID)
   json_port = json.loads(str_port)
   portfolio = jsonToPortfolio(json_port)
   
   sum_nav = 0
   my_assets = []
   for elt in portfolio.values["2016-06-01"]:
       if elt.asset:
           quotes = asset_to_quotes(elt.asset.asset, True)
           for quote in quotes:
               print(quote.nav)
               #quote_format = replace.quote.nav(",", ".")
               #sum_nav += float(quote_format.nav['value'])
               #my_assets.append({elt.asset, quote.nav})
               
   return my_assets
               
           
           
           
   
