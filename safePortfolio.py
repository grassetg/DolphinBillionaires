import json

from models.dynAmountLineAsset import DynAmountLineAsset
from apiTools import get_portfolio, get_asset
from models.portfolio import *
from models.quote import asset_to_quotes
from vars import *


def portfolioIsValid(portfolio: Portfolio, log: bool = False):
    nav = check_nav(portfolio, log)
    actions = False
    assets = False

    if nav:
        actions = check_actions(portfolio, log)
        if actions:
            assets = enough_assets(portfolio, log)

    return assets and nav and actions


def enough_assets(portfolio, log=True):
    """
    Check if there is between 15 and 40 assets in the portfolio.
    :param portfolio: a portfolio object
    :return: a boolean
    """

    nb_assets = len(portfolio.values["2016-06-01"])

    if nb_assets > 15 and nb_assets < 40:
        if log:
            print("La quantité d'action pour ce portfolio est correcte")
        return True

    if log:
        print("La quantité d'action pour ce portfolio n'est PAS correcte")
    return False


def is_uniq_compo(portfolio, log=True):
    """
    Check if the portfolio's date is "2016-06-01".
    :param portfolio: a portfolio object
    :return: a boolean
    """

    if "2016-06-01" in portfolio.values:
        if log:
            print("Ce portefeuille est une composition unique du 2016-06-01")
        return True

    if log:
        print("Ce portefeuille n'est PAS une composition unique du 2016-06-01")
    return False


def sum_nav(portfolio, log=True):
    """
    Calculate the sum of navs of all the asset from a portfolio and send a 
    dictionary of informations.
    :param portfolio: a portfolio object
    :return:
        A tupple with:
        -the sum of all of nav of the portfolio
        -a dictionary of tupples {asset_id: (nav, quantity),..., (nav, quantity)}
    """

    my_sum = 0.0
    my_assets = {}
    if "2016-06-01" in portfolio.values:
        for elt in portfolio.values["2016-06-01"]:
            if elt.asset:
                quotes = asset_to_quotes(elt.asset.asset, True, "2016-06-01", "2016-06-01")
                for quote in quotes:
                    new_nav = float(quote.nav['value'].replace(",", "."))
                    my_sum += new_nav * float(elt.asset.quantity)

                    tupple = (new_nav, elt.asset.quantity)
                    if elt.asset.asset in my_assets:
                        my_assets[elt.asset.asset].append(tupple)

                    else:
                        my_assets[elt.asset.asset] = [tupple]

    return (my_sum, my_assets)


def check_nav(portfolio, log=True):
    """
    Check if there each nav of portfolio represent a pourcent between 1% to 10%
    of the total nav.
    :param portfolio: an portfolio object
    :return: a boolean
    """

    my_sum, my_assets = sum_nav(portfolio)
    # print(my_sum, my_assets)
    for asset in my_assets:
        num = 0
        for nav, quantity in my_assets[asset]:
            num += float(nav) * float(quantity)

        pourcent = (num * 100) / my_sum
        if 1 > pourcent or pourcent > 10:
            if log:
                print("Le portefeuille ne respecte PAS la condition des navs")
            return False

    if log:
        print("Le portefeuille respecte la condition des navs")
    return True


def check_actions(portfolio, log=True):
    """
    Check if the quantity of actions is at least 50% of all the portfolio's assets.
    :param portfolio: a portfolio object
    :return: a boolean
    """

    total_count = 0
    action_count = 0
    for asset_date in portfolio.values:
        for elt in portfolio.values[asset_date]:
            total_count += int(elt.asset.quantity)

            str_asset = get_asset(elt.asset.asset, "TYPE", asset_date)
            json_asset = json.loads(str_asset)
            if json_asset["TYPE"]["value"] == "STOCK":
                action_count += elt.asset.quantity

    if total_count == 0 or action_count / total_count < 0.5:
        if log:
            print("Il n'y a PAS au moins 50% d'action dans ce portefeuille")
        return False

    if log:
        print("Il y a au moins 50% d'action dans ce portefeuille")
    return True
