import json
from random import randint

from models import *
from apiTools import *
from vars import *
from safePortfolio import enough_assets

assets_id = json.loads(get_assets(("ASSET_DATABASE_ID", "asset_fund_info_decimalisation")))
print(assets_id)
all_asset_id = []
all_asset_quantity = {}
l_asset = len(assets_id)
for i in range(l_asset):
    all_asset_id.append(int(assets_id[i]["ASSET_DATABASE_ID"]["value"]))
    if assets_id[i].has_key("asset_fund_info_decimalisation"):    
        all_asset_quantity.append(assets_id[i]["asset_fund_info_decimalisation"]["value"])


nb_asset = len(assets_id)

notes = []

print(all_asset_quantity)


def init_ptfs(nb : int = 50):
    ptfs = []
    for i in range(nb):
        list_id = []
        all_asset_id_s = all_asset_id
        for j in range(randint(15, 30)):
            choice = randint(0, nb_asset - 1 - j)
            list_id.append(all_asset_id_s[choice])
            all_asset_id_s.pop(choice)
        ptfs.append(list_id)        
    return ptfs


def ptfs_mutation(ptf, nb : int = 50):
    ptfs = []
    ptfs.append(ptf) #ajouter le ptf original/model
    #création d'une liste avec la liste des id des actifs du portefeuilles
    len_ptf = len(ptf)
    #faire pop tous les id de ptf_asset de la liste d'asset à ajouter pour les mutations
    all_asset_id_not_in_ptf = all_asset_id
    for i in range(len_ptf):
        all_asset_id_not_in_ptf.pop(all_asset_id_not_in_ptf.index(ptf[i]))
    for i in range(nb):
        list_id = ptf
        all_asset_id_s = all_asset_id_not_in_ptf
        for j in range(randint(1, 5)): #choisir le nombre d'asset qui vont changer
            change_in = randint(0, len_ptf)
            if change_in == len_ptf:
                choice = randint(0, nb_asset - 1 - j)
                list_id.append(all_asset_id_s[choice])
                all_asset_id_s.pop(choice)    
            else :
                choice = randint(0, nb_asset - 1 - j)
                list_id[change_in] = all_asset_id_s[choice]
                all_asset_id_s.pop(choice)
        ptfs.append(list_id)                
    return ptfs




#creation du portefeuille
#ptf = Portfolio(vars.PORTFOLIO_NAME, values_, currency_ , type_)