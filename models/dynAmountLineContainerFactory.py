from models.dynAmountLineAsset import DynAmountLineAsset
from models.dynAmountLineCurrency import DynAmountLineCurrency
from models.dynAmountLineContainer import DynAmountLineContainer


class DynAmountLineContainerFactory:

    def create(self, asset_, quantity_, amount_, currency_="EUR"):
        amountLineAsset = DynAmountLineAsset(asset_, quantity_)
        amountLineCurrency = DynAmountLineCurrency(amount_, currency_)

        return DynAmountLineContainer(amountLineAsset, amountLineCurrency)
