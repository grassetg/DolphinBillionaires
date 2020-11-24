import json
from random import randint
from time import strptime

from models import *
from apiTools import *
from vars import *
from safePortfolio import *
from copy import deepcopy
from safePortfolio import enough_assets

def ptfs_mutation(ptf, nb: int = 50):
    ptfs = []
    ptfs.append(ptf)
    len_ptf = len(ptf)
    asset_id_not_in_ptf = deepcopy(assets_id)
    for i in range(len_ptf):
        asset_id_not_in_ptf.pop(asset_id_not_in_ptf.index(ptf[i]))
    for i in range(nb):
        list_id = deepcopy(ptf)
        asset_id_s = deepcopy(asset_id_not_in_ptf)
        for j in range(randint(1, 5)):  # choisir le nombre d'asset qui vont changer
            change_in = randint(0, len_ptf)
            if change_in == len_ptf:
                choice = randint(0, nb_asset_id - 1 - j)
                list_id.append(asset_id_s[choice])
                asset_id_s.pop(choice)
            else:
                choice = randint(0, nb_asset_id - 1 - j)
                list_id[change_in] = asset_id_s[choice]
                asset_id_s.pop(choice)
        ptfs.append(list_id)
    return ptfs


def init_ptfs(nb: int = 50):
    ptfs = []
    ptfs_id = []
    for i in range(nb):
        list_id = []
        asset_id_copy = deepcopy(assets_id)
        values = []
        for j in range(randint(15, 30)):
            choice = randint(0, nb_asset_id - 1 - j)
            asset_id = asset_id_copy[choice]
            list_id.append(asset_id)
            asset_id_copy.pop(choice)
            if asset_id in assets_quantity:
                quantity = assets_quantity[asset_id]
            else:
                quantity = 1
            container = createAssetContainer(asset_id, quantity)
            values.append(container)
        ptfs_id.append(list_id)
        ptfs.append(Portfolio(PORTFOLIO_NAME, values, "EUR", "front"))
    return ptfs, ptfs_id


def get_best_candidate(candidates):
    notes = []
    for candidate in candidates:
        json_portfolio = json.dumps(candidate.toJson())
        # raise Exception("stop")

        put_portfolio(PORTFOLIO_ID, json_portfolio)
        print("PUT PORTFOLIO")

        sharpe = json.loads(get_sharpe([PORTFOLIO_ID], start_date="2016-06-01", end_date_="2020-09-30"))
        notes.append(sharpe["1822"]["12"]["value"])
        print("GOT SHARPE")

    index = notes.index(max(notes))
    print("all : " + str(notes))
    print()
    print("max : " + str(notes[index]))
    return index



print("--- START ---")

assets = json.loads(get_assets(("ASSET_DATABASE_ID", "asset_fund_info_decimalisation", "FIRST_QUOTE_DATE")))
assets_id = []
assets_quantity = {}
nb_asset = len(assets)

for i in range(nb_asset):
    firstQuoteDate = strptime(assets[i]["FIRST_QUOTE_DATE"]["value"], "%Y-%m-%d")
    assetId = int(assets[i]["ASSET_DATABASE_ID"]["value"])

    # Test whether the asset first quote is after the portfolio date. If it is skip this asset
    if firstQuoteDate >= strptime("2016-06-01", "%Y-%m-%d"):
        continue

    assets_id.append(assetId)

    if "asset_fund_info_decimalisation" in assets[i]:
        assets_quantity[assetId] = assets[i]["asset_fund_info_decimalisation"]["value"]

nb_asset_id = len(assets_id)


(portfolios, portfolios_id) = init_ptfs(3)
bestCandidateIndex = get_best_candidate(portfolios)
print("Le meilleur portefeuille a pour indice : ", bestCandidateIndex)