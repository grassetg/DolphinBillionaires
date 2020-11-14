
class DynAmountLineCurrency:
    """
    amount: float
    currency: str (ISO)
    """

    def __init__(self, amount_, currency_="EUR"):

        if not type(amount_) is float:
            raise Warning("A DynAmountLineCurrency object's amount should be a double/float. Was " + str(type(amount_)))

        self.currency = currency_
        self.amount = amount_
