class DynAmountLineAsset:
    """
    Quantité d'actif du portefeuille de composition historique\n
    asset: Actif\n
    quantity: Quantité de l'actif
    """

    def __init__(self, asset_: int, quantity_: float):

        self.asset = asset_
        self.quantity = quantity_