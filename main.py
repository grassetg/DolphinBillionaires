import json

from models import *
from apiTools import *
from vars import *
from safePortfolio import enough_assets


# ------------ GET ASSETS --------------
#actif = get_assets()
#allActif = json.loads(actif)
        
# print("Mes actifs")
# print(actif)

# ------------ GET QUOTES -------------
#print("Mes quotes")
#allQuotes = asset_to_quotes(allActif[1])
#allQuotes[0].print_info()

# for elt in allQuotes:
#    elt.print_info()

# print("len of my quote list " + str(len(allQuotes)))

# ------------ GET PORTFOLIO -------------
#compo = json.dumps({"label":"EPITA_PTF_3","currency":{"code":"EUR"},"type":"front","values":{"2016-06-01":[{"asset":{"asset":1845,"quantity":1.0}}]}})
#put_portfolio(1822, compo)
port = get_portfolio(PORTFOLIO_ID)
json_port = json.loads(port)
value = json_port['values']["2016-06-01"]
print(value)
print(enough_assets(value))

#{"label":"EPITA_PTF_3","currency":{"code":"EUR"},"type":"front","values":{"2016-01-16":[{"asset":{"asset":1845,"quantity":1.0}}]}}

