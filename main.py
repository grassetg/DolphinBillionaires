import json

from models import *
from apiTools import *
from vars import *
from safePortfolio import *

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
port = get_portfolio(PORTFOLIO_ID)
my_port = Portfolio(jsonToPortfolio(port))
print(my_port)
enough_asset(my_port)

