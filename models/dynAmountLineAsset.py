import json


class DynAmountLineAsset:
    """
    Quantité d'actif du portefeuille de composition historique\n
    asset: Actif\n
    quantity: Quantité de l'actif
    """

    def __init__(self, asset_: int, quantity_: float):

        if not asset_:
            raise Exception("A DynAmountLineAsset must have an asset.")

        if not quantity_:
            raise Exception("A DynAmountLineAsset must have a currency.")

        self.asset = asset_
        self.quantity = quantity_


def jsonToDynAmountLineAsset(jsonAsset):
    dictionary = None

    if type(jsonAsset) is str:
        dictionary = json.loads(jsonAsset)
    elif type(jsonAsset) is dict:
        dictionary = jsonAsset

    asset = DynAmountLineAsset(dictionary['asset'], dictionary['quantity'])

    return asset
