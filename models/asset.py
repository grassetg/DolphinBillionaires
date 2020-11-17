    # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import urllib3
import json
urllib3.disable_warnings()

class Asset:
    def __init__(self, lastCloseValueInCurr, label, assetType, assetDatabaseId) :    
        self.lastCloseValueInCurr = lastCloseValueInCurr 
        lastCloseValueInCurr.replace(',', '.')
        indexspace = lastCloseValueInCurr.index(' ')
        self.lastCloseValueInCurrAmount = float(lastCloseValueInCurr[0:indexspace])
        self.lastCloseValueInCurrCurrency = lastCloseValueInCurr[indexspace+1:]
        self.label = label
        self.assetType = assetType
        self.assetDatabaseId = assetDatabaseId
        
def json_to_many_asset(asset):
    l_asset = len(asset)
    asset_v = []
    for i in range(l_asset):
        try:
            asset_v.append(Asset(asset[i]['LAST_CLOSE_VALUE_IN_CURR']['value'], int(asset[i]['ASSET_DATABASE_ID']['value']), asset[i]['LABEL']['value'], asset[i]['TYPE']['value']))
        except:
            asset_v.append(Asset('-1 NOCURR', int(asset[i]['ASSET_DATABASE_ID']['value']), asset[i]['LABEL']['value'], asset[i]['TYPE']['value']))
    return asset_v

def json_to_one_asset(asset):
    try:
        return (Asset(asset['LAST_CLOSE_VALUE_IN_CURR']['value'], int(asset['ASSET_DATABASE_ID']['value']), asset['LABEL']['value'], asset['TYPE']['value']))
    except:
        return (Asset('-1 NOCURR', int(asset['ASSET_DATABASE_ID']['value']), asset['LABEL']['value'], asset['TYPE']['value']))



#Notre portefeuille à nous rien qu'à nous : 1822
#'LAST_CLOSE_VALUE_IN_CURR': {'type': 'currency_value', 'value': '40,272 EUR'}
#'ASSET_DATABASE_ID': {'type': 'int32', 'value': '1984'}
#'LABEL': {'type': 'string', 'value': 'ZOOPLUS AG'} 
#'TYPE': {'type': 'asset_type', 'value': 'STOCK'}

























