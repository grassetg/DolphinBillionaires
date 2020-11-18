import json


class DynAmountLineCurrency:
    """
    Valeur monétaire du portefeuille de composition historique\n
    amount: Montant de la devise. Attention, ce montant doit être fournis en devise de portefeuille.\n
    currency: Devise. L'identifiant est le code ISO 4217 de la devise
    """

    def __init__(self, amount_: float, currency_: str = "EUR"):
        self.currency = currency_
        self.amount = amount_


def jsonToDynAmountLineCurrency(jsonCurrency):
    dictionary = dict()

    if type(jsonCurrency) is str:
        dictionary = json.loads(jsonCurrency)
    elif type(jsonCurrency) is dict:
        dictionary = jsonCurrency

    if dictionary.keys().__contains__("currency"):
        currency = DynAmountLineCurrency(dictionary['amount'], dictionary["currency"])
    else:
        currency = DynAmountLineCurrency(dictionary['amount'])

    return currency
