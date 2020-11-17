from models.dynAmountLineAsset import DynAmountLineAsset
from models.dynAmountLineCurrency import DynAmountLineCurrency


class DynAmountLineContainer:
    """
    Container pour une valeur d'un portefeuille de composition historique. Une seul de ses valeurs peut être non nulle a la fois.
    asset: DynAmountLineAsset\n
    currency: DynAmountLineCurrency
    """

    def __init__(self, asset_, currency_):

        if not type(asset_) is DynAmountLineAsset:
            raise TypeError("A DynAmountLineContainer object's asset must be a DynAmountLineAsset object")

        if not type(currency_) is DynAmountLineCurrency:
            raise TypeError("A DynAmountLineContainer object's currency must be a DynAmountCurrency object")

        self.asset = asset_
        self.currency = currency_
