# -*- coding: utf-8 -*-
from models.dynAmountLineAsset import DynAmountLineAsset

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
