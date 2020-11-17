import string
from typing import List

from models.dynAmountLineContainer import DynAmountLineContainer


class Portfolio:
    """
    Portefeuille de composition historique
    label : Nom du portefeuille\n
    currency : Devise. L'identifiant est le code ISO 4217 de la devise\n
    values : Contenu du portefeuille par date. Les clés de cet objet sont au format 'date'\n
    type: Type de portfolio DynAmount : soit "front" soit "back"
    """

    def __init__(self, label_: str, type_: str, values_: List[DynAmountLineContainer], currency_: str = "EUR"):

        if type_ != "front" and type_ != "ack":
            raise Exception("A portfolio's type must be \"front\" or \"back\"?")

        if not type(label_) is string:
            raise TypeError("A portfolio's label must be a string.")

        for ele in values_:
            if not type(ele) is DynAmountLineContainer:
                raise TypeError("A portfolio's values attribute must be an iterable of DynAmountLineContainer.")

        self.label = label_
        self.currency = currency_
        self.type = type_
        self.values = {"2013-06-14": values_}
