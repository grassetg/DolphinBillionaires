import json

from models import *
from apiTools import *

# ------------ GET ASSETS --------------
actif = get_assets("/asset")
allActif = json.loads(actif)
# print("Mes actifs")
# print(actif)

# ------------ GET QUOTES -------------
print("Mes quotes")
allQuotes = asset_to_quotes(allActif[1])

allQuotes[0].print_info()

# for elt in allQuotes:
#    elt.print_info()

# print("len of my quote list " + str(len(allQuotes)))

