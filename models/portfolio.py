import string


class Portfolio:
    """
    label : name of the portfolio
    currency : ISO code of the currency, set to "EUR" by default
    values : dict with an entry named 2013-06-14 and holding the portfolio's entries
    type: either "front" or "back"
    """

    def __init__(self, label_, type_, values_, currency_="EUR"):

        if type_ != "front" and type_ != "ack":
            raise Exception("A portfolio's type must be \"front\" or \"back\"?")

        if not type(label_) is string:
            raise TypeError("A portfolio's label must be a string.")

        self.label = label_
        self.currency = currency_
        self.type = type_
        self.values = {"2013-06-14": values_}
