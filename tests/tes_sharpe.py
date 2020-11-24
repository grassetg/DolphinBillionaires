from models import *
from apiTools import *
from vars import *
import json

jsonPort = json.dumps(
    {
        "currency": {
            "code": "EUR"
        },
        "label": "Front_test_dyn",
        "type": "front",
        "values": {
            "2016-06-01": [
                {
                    "asset": {
                        "asset": 1845,
                        "quantity": 1
                    }
                },
                {
                    "asset": {
                        "asset": 1991,
                        "quantity": 1
                    }
                }
            ]
        }
    })

portfolio = jsonToPortfolio(get_portfolio(PORTFOLIO_ID))

portfolio_sharpe = get_sharpe([PORTFOLIO_ID], start_date="2016-06-01", end_date_="2016-06-02")
asset_sharpe = get_portfolio_sharpe(portfolio, start_date="2016-06-01", end_date_="2016-06-02")

"""
asset1 = json.loads(get_quotes(1845,"2016-05-01", "2020-09-30"))
asset2 = json.loads(get_quotes(1991, "2016-06-01", "2020-09-30"))"""


print("porfolio : " + portfolio_sharpe)
print("asset : " + asset_sharpe)

"""
for i in range(51):
    print( str(asset1[i]["date"]["value"]) + " : " + str(asset1[i]["nav"]["value"]))
"""

#print("1991 : " + asset2)
