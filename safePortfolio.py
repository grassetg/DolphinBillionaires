# -*- coding: utf-8 -*-
from models.dynAmountLineAsset import DynAmountLineAsset

def enough_assets(portfolio):
    count = 0
    for elt in portfolio:
        if elt['asset']:
            count += float(elt['asset']['quantity'])
        
    return count > 15 and count < 40
