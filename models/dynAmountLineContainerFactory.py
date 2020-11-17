from models.dynAmountLineAsset import DynAmountLineAsset
from models.dynAmountLineCurrency import DynAmountLineCurrency
from models.dynAmountLineContainer import DynAmountLineContainer


class DynAmountLineContainerFactory:
    """
    Factory for DynAmountLineContainers
    """

    def create(self, asset_: int, quantity_: float, amount_: float, currency_: str = "EUR"):
        """
        :param asset_: the asset's db id
        :param quantity_: asset quantity
        :param amount_: amount invested
        :param currency_: iso code of the currency
        :return: the matching dynAmountLineContainer
        """
        amountLineAsset = DynAmountLineAsset(asset_, quantity_)
        amountLineCurrency = DynAmountLineCurrency(amount_, currency_)

        return DynAmountLineContainer(amountLineAsset, amountLineCurrency)
