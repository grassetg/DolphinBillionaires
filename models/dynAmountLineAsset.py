class DynAmountLineAsset:
    """
    asset: int
    quantity: float
    """

    def __init__(self, asset_, quantity_):

        if not type(asset_) is int:
            TypeError("A DynAmountLineAsset object's asset attribute must be an int.")

        if not type(quantity_) is float:
            TypeError("A DynAmountLineAsset object's quantity attribute must be an double/float.")

        self.asset = asset_
        self.quantity = quantity_
