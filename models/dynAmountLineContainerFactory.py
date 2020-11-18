from models.dynAmountLineAsset import DynAmountLineAsset
from models.dynAmountLineCurrency import DynAmountLineCurrency
from models.dynAmountLineContainer import DynAmountLineContainer


class DynAmountLineContainerFactory:
    """
    Factory for DynAmountLineContainers
    """

    def createAssetContainer(self, asset_: int, quantity_: float):
        """
        :param asset_: the asset's db id
        :param quantity_: asset quantity
        :return: the matching dynAmountLineContainer with asset
        """

        amountLineAsset = DynAmountLineAsset(asset_, quantity_)
        return DynAmountLineContainer(amountLineAsset, None)

    def createCurrencyContainer(self, amount_: float, currency_: str = "EUR"):
        """
        :param amount_: amount invested
        :param currency_: iso code of the currency
        :return: the matching dynAmountLineContainer with currency
        """

        amountLineCurrency = DynAmountLineCurrency(amount_, currency_)
        return DynAmountLineContainer(None, amountLineCurrency)
