import requests

from vars import URL, AUTH


def get_asset(assetId, date=None, full_response=False):
    parameters = {'date': date, 'fullResponse': full_response}
    res = requests.get(URL + "/asset/" + assetId,
                       params=parameters,
                       auth=AUTH,
                       verify=False)
    return res.content.decode('utf-8')


def get_assets(columns=("ASSET_DATABASE_ID", "LABEL", "TYPE", "LAST_CLOSE_VALUE_IN_CURR"),
               date="2013-06-14", full_response=False):
    parameters = {'date': date, 'fullResponse': full_response, 'columns': columns}
    res = requests.get(URL + '/asset/',
                       params=parameters,
                       auth=AUTH,
                       verify=False)
    return res.content.decode('utf-8')


def get_asset_attribute(assetId, attributeName, date=None, full_response=False):
    parameters = {'date': date, 'fullResponse': full_response}
    res = requests.get(URL + "/asset/" + assetId + "/attribute/" + attributeName,
                       params=parameters,
                       auth=AUTH,
                       verify=False)
    return res.content.decode('utf-8')


def get_quotes(data_id):
    parameters = {'id': int(data_id), 'start_quotes': "1985-04-12", 'end_quotes': "2020-11-17"}
    res = requests.get(URL + "/asset/" + data_id + "/quote",
                       params=parameters,
                       auth=AUTH,
                       verify=False)

    return res.content.decode('utf-8')


def get_portfolio(portfolioId):
    parameters = {}
    res = requests.get(URL + "/portfolio/" + portfolioId + "/dyn_amount_compo",
                       params=parameters,
                       auth=AUTH,
                       verify=False)

    return res.content.decode('utf-8')


def put_portfolio(portfolioId, portfolio):
    parameters = {}
    res = requests.put(URL + "/portfolio/" + portfolioId + "/dyn_amount_compo",
                       params=parameters,
                       auth=AUTH,
                       body=portfolio,
                       verify=False)

    return res.content.decode('utf-8')


def get_ratios():
    parameters = {}
    res = requests.put(URL + "/ratio/",
                       params=parameters,
                       auth=AUTH,
                       verify=False)

    return res.content.decode('utf-8')


def post_ratios(ratio, fullResponse: bool = False):
    parameters = {"fullResponse": fullResponse}
    res = requests.put(URL + "/ratio/invoke",
                       params=parameters,
                       auth=AUTH,
                       body=ratio,
                       verify=False)

    return res.content.decode('utf-8')
