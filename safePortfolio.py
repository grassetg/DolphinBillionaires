# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:16:49 2020

@author: 33667
"""

def enough_assets(portfolio):
    count = 0
    for container in portfolio.values:
        if container.asset:
            count += 1
        
    return portfolio.asset < 15 or portfolio.asset > 40
