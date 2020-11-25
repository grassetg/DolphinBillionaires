import json
import string
from typing import List

from models.dynAmountLineContainer import DynAmountLineContainer, jsonToDynAmountLineContainer


class Portfolio:
    """
    Portefeuille de composition historique
    label : Nom du portefeuille\n
    currency : Devise. L'identifiant est le code ISO 4217 de la devise\n
    values : Contenu du portefeuille par date. Les clés de cet objet sont au format 'date'\n
    type: Type de portfolio DynAmount : soit "front" soit "back"
    """

    def __init__(self, label_: str, values_: List[DynAmountLineContainer], currency_: str = "EUR", type_: str = "front"):

        if type_ != "front" and type_ != "ack":
            raise Exception("A portfolio's type must be \"front\" or \"back\"?")

        for ele in values_:
            if not type(ele) is DynAmountLineContainer:
                raise TypeError("A portfolio's values attribute must be an iterable of DynAmountLineContainer.")

        self.label = label_
        self.currency = currency_
        self.type = type_
        self.values = {"2016-06-01": values_}

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


def jsonToPortfolio(jsonPortfolio, date: str = "2016-06-01"):
    dictionary = dict()

    if type(jsonPortfolio) is str:
        dictionary = json.loads(jsonPortfolio)
    elif type(jsonPortfolio) is dict:
        dictionary = jsonPortfolio

    values = []
    print(date)
    for value in dictionary["values"][date]:
        container = jsonToDynAmountLineContainer(value)
        values.append(container)

    portfolio = Portfolio(dictionary["label"], values, dictionary.get("currency", "EUR"),
                          dictionary.get("type", None))
    return portfolio
