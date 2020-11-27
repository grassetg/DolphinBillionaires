import json
from random import randint
from time import strptime

from models import *
from apiTools import *
from vars import *
from safePortfolio import *
from copy import deepcopy
from safePortfolio import *

logFile = open("algo2.log", "a")
assets = json.loads(get_assets(("ASSET_DATABASE_ID", "asset_fund_info_decimalisation", "FIRST_QUOTE_DATE")))
assets_ids = []
assets_quantity = {}
nb_asset = len(assets)

for i in range(nb_asset):
    firstQuoteDate = strptime(assets[i]["FIRST_QUOTE_DATE"]["value"], "%Y-%m-%d")
    assetId = int(assets[i]["ASSET_DATABASE_ID"]["value"])

    # Test whether the asset first quote is after the portfolio date. If it is skip this asset
    if firstQuoteDate >= strptime("2016-06-01", "%Y-%m-%d"):
        continue

    assets_ids.append(assetId)

    if "asset_fund_info_decimalisation" in assets[i]:
        assets_quantity[assetId] = assets[i]["asset_fund_info_decimalisation"]["value"]

nb_asset_id = len(assets_ids)


def ptfs_mutation(ptf_ids, nb: int = 50):
    ptfs_id = []
    ptfs_id.append(ptf_ids)
    len_ptf = len(ptf_ids)
    asset_id_not_in_ptf = deepcopy(assets_ids)
    nbValidsPtfs = 0

    for i in range(len_ptf):
        asset_id_not_in_ptf.pop(asset_id_not_in_ptf.index(ptf_ids[i])) # Enleve les ids du ptf à la totalité des ids

    for i in range(nb):
        list_id = deepcopy(ptf_ids)
        asset_id_s = deepcopy(asset_id_not_in_ptf)
        nbAssetsIdSave = len(asset_id_s)
        for j in range(randint(1, 5)):  # choisir le nombre d'asset qui vont changer
            change_in = randint(0, len_ptf + 1)
            if change_in >= len_ptf:
                choice = randint(0, nbAssetsIdSave - 1 - j)
                list_id.append(asset_id_s[choice])
                asset_id_s.pop(choice)
            else:
                choice = randint(0, nbAssetsIdSave - 1 - j)
                list_id[change_in] = asset_id_s[choice]
                asset_id_s.pop(choice)
        ptfs_id.append(list_id)
    return ptfs_id


def init_ptfs(nb: int = 50, maxTries=80):
    ptfs = []
    ptfs_id = []
    total_tries = 0
    nbValidPtfs = 0
    for i in range(nb):
        validPortfolio = False
        nbTries = 0
        while not validPortfolio and nbTries < maxTries:
            list_id = []
            asset_id_copy = deepcopy(assets_ids)
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
            nbTries += 1
            total_tries += 1
            ptf = Portfolio(PORTFOLIO_NAME, values, "EUR", "front")
            validPortfolio = portfolioIsValid(ptf)

            if validPortfolio or nbTries == maxTries:
                if validPortfolio:
                    nbValidPtfs += 1
                    txt = "VALID"
                    print(txt)
                    logFile.write("VALID : " + str(ptf.toJson()) + "\n")
                ptfs_id.append(list_id)
                ptfs.append(ptf)
            else:
                txt = "Non valide ( " + str(i) + "/" + str(nb) + " , " + str(nbTries) + "tries )"
                print(txt)
                logFile.write(txt + "\n")

    return ptfs, ptfs_id, nbValidPtfs


def get_best_candidate(candidates):
    currentPortfolio = get_portfolio(PORTFOLIO_ID)
    notes = []
    for candidate in candidates:
        json_portfolio = json.dumps(candidate.toJson())
        # raise Exception("stop")

        put_portfolio(PORTFOLIO_ID, json_portfolio)
        logFile.write("PUT PORTFOLIO\n")
        print("PUT PORTFOLIO")

        sharpe = json.loads(get_sharpe([PORTFOLIO_ID], start_date="2016-06-01", end_date_="2020-09-30"))
        notes.append(sharpe["1822"]["12"]["value"])
        logFile.write("GOT SHARPE\n")
        print("GOT SHARPE")

    index = notes.index(max(notes))
    print("all : " + str(notes))
    print()
    print("max : " + str(notes[index]))
    put_portfolio(PORTFOLIO_ID, currentPortfolio)
    return index


def ptfsIdsToPortfolios(ptfs_ids):
    ptfs = []
    nbValidPtfs = 0
    index = 0
    total = len(ptfs_ids)
    for list_id in ptfs_ids:
        index += 1
        print("Checking ptfs for valid candidates ... ", index, "/", total)
        values = []

        for asset_id in list_id:
            if asset_id in assets_quantity:
                quantity = assets_quantity[asset_id]
            else:
                quantity = 1
            container = createAssetContainer(asset_id, quantity)
            values.append(container)

        ptf = Portfolio(PORTFOLIO_NAME, values, "EUR", "front")
        ptfs.append(ptf)
        if portfolioIsValid(ptf):
            nbValidPtfs += 1
            print("VALID : " + ptf.toJson())
            logFile.write("VALID : " + ptf.toJson() + "\n")
            logFile.flush()

    return ptfs, nbValidPtfs


def algorithm(nbPtfsToGenerate=5):
    logFile.write("===============================\n")
    logFile.write("--- START ---\n")
    print("--- START ---")
    currentSharpe = \
        json.loads(get_sharpe([PORTFOLIO_ID], start_date="2016-06-01", end_date_="2020-09-30"))["1822"]["12"]["value"]
    bestCandidateIndex = -1
    (portfolios, portfolios_ids, nbValidPtfs) = init_ptfs(nbPtfsToGenerate, 1)
    print("INIT DONE")

    while bestCandidateIndex == -1 or nbValidPtfs < 1:
        if bestCandidateIndex == -1:
            bestCandidateIndex = 0
        portfolios_ids = ptfs_mutation(portfolios_ids[bestCandidateIndex])
        print("MUTATION DONE")
        portfolios, nbValidPtfs = ptfsIdsToPortfolios(portfolios_ids)
        print("COUNTED VALID PTFS : ", nbValidPtfs)

    logFile.flush()
    bestCandidateIndex = get_best_candidate(portfolios)

    print("Le meilleur portefeuille a pour indice : ", bestCandidateIndex)
    bestCandidate = portfolios[bestCandidateIndex]
    print(bestCandidate.toJson())
    print()

    # Criteria tests
    enough_assets(bestCandidate)
    check_actions(bestCandidate)
    check_nav(bestCandidate)
    print()

    print("Current Sharpe is", str(currentSharpe))
    wantPut = input("Do you want to put this candidate ? (y/n)")
    if wantPut == "y" or wantPut == "Y":
        put_portfolio(PORTFOLIO_ID, json.dumps(bestCandidate.toJson()))
        print("Put candidate")
    print("--- END ---")


algorithm()
logFile.close()
