import json

from models.dynAmountLineAsset import DynAmountLineAsset
from models.dynAmountLineCurrency import DynAmountLineCurrency


class DynAmountLineContainer:
    """
    Container pour une valeur d'un portefeuille de composition historique. Une seul de ses valeurs peut être non nulle a la fois.
    asset: DynAmountLineAsset\n
    currency: DynAmountLineCurrency
    """

    def __init__(self, asset_: DynAmountLineAsset = None, currency_: DynAmountLineCurrency = None):

        if not asset_ and not currency_:
            raise Exception("Either asset or currency must be set in DynAmountLineCurrency.")

        elif asset_ and currency_:
            raise Exception("Cannot have both asset and currency in one DynAmountLineCurrency.")

        self.asset = asset_
        self.currency = currency_


def jsonToDynAmountLineContainer(jsonContainer):
    dictionary = dict()

    if type(jsonContainer) is str:
        dictionary = json.loads(jsonContainer)
    elif type(jsonContainer) is dict:
        dictionary = jsonContainer

    if dictionary.keys().__contains__("currency"):

        currency = DynAmountLineCurrency.jsonToDynAmountLineCurrency(dictionary["currency"])
        return DynAmountLineContainer(None, currency)

    else:

        asset = DynAmountLineAsset.jsonToDynAmountLineAsset(dictionary['asset'])
        return DynAmountLineContainer(asset, None)


def createCurrencyContainer(amount_: float, currency_: str = "EUR"):
    """
    :param amount_: amount invested
    :param currency_: iso code of the currency
    :return: the matching dynAmountLineContainer with currency
    """

    amountLineCurrency = DynAmountLineCurrency(amount_, currency_)
    return DynAmountLineContainer(None, amountLineCurrency)


def createAssetContainer(asset_: int, quantity_: float):
    """
    :param asset_: the asset's db id
    :param quantity_: asset quantity
    :return: the matching dynAmountLineContainer with asset
    """

    amountLineAsset = DynAmountLineAsset(asset_, quantity_)
    return DynAmountLineContainer(amountLineAsset, None)
