class DynAmountLineAsset:
    """
    Quantité d'actif du portefeuille de composition historique\n
    asset: Actif\n
    quantity: Quantité de l'actif
    """

    def __init__(self, asset_ : int, quantity_: float):

        if not type(asset_) is int:
            TypeError("A DynAmountLineAsset object's asset attribute must be an int.")

        if not type(quantity_) is float:
            TypeError("A DynAmountLineAsset object's quantity attribute must be an double/float.")

        self.asset = asset_
        self.quantity = quantity_

    def jsonToDyn(self, json):
        self.asset = json["asset"]
        self.quantity = json["quantity"]


def jsonToDyn2( json):
    return DynAmountLineAsset(json["asset"], json["quantity"])