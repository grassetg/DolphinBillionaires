from typing import List

import requests

from models.dynAmountLineContainer import DynAmountLineContainer
from models.ratioParamMultiAsset import RatioParamMultiAsset
from vars import URL, AUTH


def get_asset(assetId, date=None, full_response=False):
    parameters = {'date': date, 'fullResponse': full_response}
    res = requests.get(URL + "/asset/" + str(assetId),
                       params=parameters,
                       auth=AUTH,
                       verify=False)

    if res.status_code != 200:
        errorHandling(res)
        return res

    return res.content.decode('utf-8')


def get_assets(columns=("ASSET_DATABASE_ID", "LABEL", "TYPE", "LAST_CLOSE_VALUE_IN_CURR"),
               date="2013-06-14", full_response=False):
    parameters = {'date': date, 'fullResponse': full_response, 'columns': columns}
    res = requests.get(URL + '/asset/',
                       params=parameters,
                       auth=AUTH,
                       verify=False)

    if res.status_code != 200:
        errorHandling(res)
        return res

    return res.content.decode('utf-8')


def get_asset_attribute(assetId, attributeName, date=None, full_response=False):
    parameters = {'date': date, 'fullResponse': full_response}
    res = requests.get(URL + "/asset/" + str(assetId) + "/attribute/" + attributeName,
                       params=parameters,
                       auth=AUTH,
                       verify=False)

    if res.status_code != 200:
        errorHandling(res)
        return res

    return res.content.decode('utf-8')


def get_quotes(data_id):
    parameters = {'id': int(data_id), 'start_quotes': "1985-04-12", 'end_quotes': "2020-11-17"}
    res = requests.get(URL + "/asset/" + str(data_id) + "/quote",
                       params=parameters,
                       auth=AUTH,
                       verify=False)

    if res.status_code != 200:
        errorHandling(res)
        return res

    return res.content.decode('utf-8')


def get_portfolio(portfolioId):
    parameters = {}
    res = requests.get(URL + "/portfolio/" + portfolioId + "/dyn_amount_compo",
                       params=parameters,
                       auth=AUTH,
                       verify=False)

    if res.status_code != 200:
        errorHandling(res)
        return res

    return res.content.decode('utf-8')


def put_portfolio(portfolioId, portfolio):
    parameters = portfolio
    res = requests.put(URL + "/portfolio/" + str(portfolioId) + "/dyn_amount_compo",
                       params=parameters,
                       auth=AUTH,
                       data=portfolio,
                       verify=False)

    if res.status_code != 200:
        errorHandling(res)
        return res

    return res.content.decode('utf-8')


def get_ratios(endpointApi='/ratio', date=None, full_response=False):
    payload = {'date': date, 'fullResponse': full_response}
    res = requests.get(URL + endpointApi,
                       params=payload,
                       auth=AUTH,
                       verify=False)

    if res.status_code != 200:
        errorHandling(res)
        return res

    return res.content.decode('utf-8')


def post_ratios(ratio: RatioParamMultiAsset, fullResponse: bool = False):
    parameters = {"fullResponse": fullResponse}
    res = requests.post(URL + "/ratio/invoke",
                        params=parameters,
                        auth=AUTH,
                        data=ratio,
                        verify=False)

    if res.status_code != 200:
        errorHandling(res)
        return res

    return res.content.decode('utf-8')


def get_sharpe(asset: List[int], benchmark: int = None, start_date: str = None,
               end_date_: str = None, frequency_: str = None, fullResponse: bool = False):
    sharpeId = 12
    ratioParam = RatioParamMultiAsset([sharpeId], asset, benchmark, start_date, end_date_, frequency_)
    return post_ratios(ratioParam.toJson(), fullResponse)


def errorHandling(res):
    print('(error): The http communication failed with code ' + str(res.status_code))
    print(res)
