import json


class Ratio:
    """
    Structure d'un ratio
    """

    def __init__(self, id_: int, type_: str = None, name_: str = None, is_benchmark_needed_: bool = None,
                 is_percent_: bool = None):
        self.id = id_
        self.type = type_
        self.name = name_
        self.is_benchmark_needed = is_benchmark_needed_
        self.is_percent = is_percent_

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @staticmethod
    def jsonToRatio(jsonRatio: json):
        dictionary = None

        if type(jsonRatio) is str:
            dictionary = json.loads(jsonRatio)
        elif type(jsonRatio) is dict:
            dictionary = jsonRatio

        if not dictionary['id']:
            raise Exception("A ratio must have an id.")

        ratio = Ratio(dictionary['id'])

        for key in dictionary.keys():
            ratio.__dict__[key] = dictionary[key]

        return ratio
