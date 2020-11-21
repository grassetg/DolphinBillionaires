import json

from models.dynAmountLineAsset import DynAmountLineAsset
from apiTools import get_portfolio
from models.portfolio import jsonToPortfolio
from models.quote import asset_to_quotes
from vars import *


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


def sum_nav(portfolio):
    my_sum = 0
    my_assets = {}
    for elt in portfolio.values["2016-06-01"]:
        if elt.asset:
            quotes = asset_to_quotes(elt.asset.asset, True)
            for quote in quotes:
                new_nav = float(quote.nav['value'].replace(",", "."))
                my_sum += new_nav * elt.asset.quantity
                
                tupple = (new_nav, elt.asset.quantity)
                if elt.asset.asset in my_assets:
                    my_assets[elt.asset.asset].append(tupple)
                    
                else:
                    my_assets[elt.asset.asset] = [tupple]
                
    return (my_sum, my_assets)

def check_nav(port_ID):
    str_port = get_portfolio(port_ID)
    json_port = json.loads(str_port)
    portfolio = jsonToPortfolio(json_port)
    
    my_sum, my_assets = sum_nav(portfolio)
    for asset in my_assets:
        num = 0
        print (asset)
        for nav, quantity in my_assets[asset]:
            num += nav * quantity
         
        pourcent = (num * 100) / my_sum       
        print(pourcent)
        if  1 > pourcent or pourcent > 10:
            print("Le portefeuille ne respecte PAS la condition des navs")
            return False
        
    print("Le portefeuille respecte la condition des navs")
    return True
               
           
           
           
   
