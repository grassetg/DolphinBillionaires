class DynAmountLineCurrency:
    """
    Valeur monétaire du portefeuille de composition historique\n
    amount: Montant de la devise. Attention, ce montant doit être fournis en devise de portefeuille.\n
    currency: Devise. L'identifiant est le code ISO 4217 de la devise
    """

    def __init__(self, amount_: float, currency_: str = "EUR"):
        self.currency = currency_
        self.amount = amount_
