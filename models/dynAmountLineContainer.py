from models.dynAmountLineAsset import DynAmountLineAsset
from models.dynAmountLineCurrency import DynAmountLineCurrency


class DynAmountLineContainer:
    """
    Container pour une valeur d'un portefeuille de composition historique. Une seul de ses valeurs peut être non nulle a la fois.
    asset: DynAmountLineAsset\n
    currency: DynAmountLineCurrency
    """

    def __init__(self, asset_: DynAmountLineAsset, currency_: DynAmountLineCurrency):

        if not asset_ and not currency_:
            raise Exception("Either asset or currency must be set in DynAmountLineCurrency.")

        elif asset_ and currency_:
            raise Exception("Cannot have both asset and currency in one DynAmountLineCurrency.")

        self.asset = asset_
        self.currency = currency_
