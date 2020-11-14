from models.dynAmountLineAsset import DynAmountLineAsset
from models.dynAmountLineCurrency import DynAmountLineCurrency

class DynAmountLineContainer:
    """
    TODO
    """

    def __init__(self, asset_, currency_):

        if not type(asset_) is DynAmountLineAsset:
            raise TypeError("A DynAmountLineContainer object's asset must be a DynAmountLineAsset object")

        if not type(currency_) is DynAmountLineCurrency:
            raise TypeError("A DynAmountLineContainer object's currency must be a DynAmountCurrency object")
        self.asset = asset_
        self.currency = currency_