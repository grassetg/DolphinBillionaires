import json
from random import randint

from models import *
from apiTools import *
from vars import *
from safePortfolio import *
from copy import deepcopy
from safePortfolio import enough_assets
    
               
assets = json.loads(get_assets(("ASSET_DATABASE_ID", "asset_fund_info_decimalisation")))
assets_id = []
assets_quantity = {}
nb_asset = len(assets)

for i in range(nb_asset):
    id = int(assets[i]["ASSET_DATABASE_ID"]["value"])
    assets_id.append(id)
    if "asset_fund_info_decimalisation" in assets[i]:
        assets_quantity[id] = assets[i]["asset_fund_info_decimalisation"]["value"]



def init_ptfs(nb : int = 50):
    ptfs = []
    for i in range(nb):
        list_id = []
        all_asset_id_s = all_asset_id
        for j in range(randint(15, 30)):
            choice = randint(0, nb_asset - 1 - j)
            list_id.append(all_asset_id_s[choice])
            all_asset_id_s.pop(choice)
        ptfs.append(list_id)        
    return ptfs


def ptfs_mutation(ptf, nb : int = 50):
    ptfs = []
    ptfs.append(ptf) #ajouter le ptf original/model
    #création d'une liste avec la liste des id des actifs du portefeuilles
    len_ptf = len(ptf)
    #faire pop tous les id de ptf_asset de la liste d'asset à ajouter pour les mutations
    all_asset_id_not_in_ptf = all_asset_id
    for i in range(len_ptf):
        all_asset_id_not_in_ptf.pop(all_asset_id_not_in_ptf.index(ptf[i]))
    for i in range(nb):
        list_id = ptf
        all_asset_id_s = all_asset_id_not_in_ptf
        for j in range(randint(1, 5)): #choisir le nombre d'asset qui vont changer
            change_in = randint(0, len_ptf)
            if change_in == len_ptf:
                choice = randint(0, nb_asset - 1 - j)
                list_id.append(all_asset_id_s[choice])
                all_asset_id_s.pop(choice)    
            else :
                choice = randint(0, nb_asset - 1 - j)
                list_id[change_in] = all_asset_id_s[choice]
                all_asset_id_s.pop(choice)
        ptfs.append(list_id)                
    return ptfs


'''
def init_ptfs(nb: int = 50):
    ptfs = []
    for i in range(nb):
        list_id = []
        asset_id_copy = deepcopy(assets_id)
        values = []

        for j in range(randint(15, 30)):
            choice = randint(0, nb_asset - 1 - j)
            asset_id = asset_id_copy[choice]
            list_id.append(asset_id)
            asset_id_copy.pop(choice)

            if asset_id in assets_quantity:
                quantity = assets_quantity[asset_id]
            else:
                quantity = 1

            container = createAssetContainer(asset_id, quantity)
            values.append(container)
        ptfs.append(Portfolio(PORTFOLIO_NAME, values, "EUR", "front"))

    return ptfs
'''

porfolios = init_ptfs(10)

'''
def get_best_candidate(portfolios):
    notes = []
    for portfolio in portfolios:
        print(portfolio.toJson())
        raise Exception("stop")
        put_portfolio(PORTFOLIO_ID, portfolio.toJson())
        print("PUT PORTFOLIO")
        sharpe = json.loads(get_sharpe(PORTFOLIO_ID, start_date="2016-06-01", end_date_="2020-09-30"))
        notes.append(sharpe["1822"]["12"]["value"])
        print("GOT SHARPE")

    index = notes.index(max(notes))
    print("all : " + str(notes))
    print()
    print("max : " + str(notes[index]))
    return portfolios[index]


print(get_best_candidate(porfolios))
'''

# creation du portefeuille
# ptf = Portfolio(vars.PORTFOLIO_NAME, values_, currency_ , type_)
