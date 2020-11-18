import json
from typing import List


class RatioParamMultiAsset:
    """
    ratiosIds : Id des ratios à éxécuter
    assetsIds : Id des actifs sur lesquels éxécuter le ratio
    benchmark: Benchmark pour le ratio, Peut être nécessaire selon les ratios, voir la propriété du ratio 'is_benchmark_needed'
    startDate: Date de debut pour le ratio, Peut être nécessaire selon les ratios
    endDate: Date de fin pour le ratio, Peut être nécessaire selon les ratios
    frequency: Fréquence
    """

    def __init__(self, ratio_: List[int], asset_: List[int], benchmark_: int = None, start_date_: str = None,
                 end_date_: str = None, frequency_: str = None):
        if frequency_ != "daily" and frequency_ != "monthly" and frequency_ != "weekly" and frequency_ != "yearly":
            raise ValueError("Ratio frequency must be one of daily/monthly/weekly/yearly.")

        self.ratio = ratio_
        self.asset = asset_
        self.benchmark = benchmark_
        self.start_date = start_date_
        self.end_date = end_date_
        self.frequency = frequency_

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


def jsonToRatioParamMultiAsset(jsonRatioParam):
    dictionary = dict()

    if type(jsonRatioParam) is str:
        dictionary = json.loads(jsonRatioParam)
    elif type(jsonRatioParam) is dict:
        dictionary = jsonRatioParam

    ratioParam = RatioParamMultiAsset(dictionary['ratio'], dictionary["asset"])

    for key in dictionary.keys():
        if key == "ratio" or key == "asset":
            continue

        ratioParam.__dict__[key] = dictionary[key]

    return ratioParam
