import json
import unittest
from safePortfolio import *
from models.portfolio import *
    
class SafePortfolioTests(unittest.TestCase):
    
    our_port = get_portfolio(PORTFOLIO_ID)
    port = json.dumps({"label":"HI_TEST","currency":{"code":"EUR"},"type":"front","values":{"2015-06-01":[{"asset":{"asset":1845,"quantity":1.0}}]}})
    port1 = json.dumps({"label":"HI_TEST1","currency":{"code":"EUR"},"type":"front","values":{"2016-06-01":[{"asset":{"asset":1845,"quantity":1.0}}]}})
    port2 = json.dumps({"label":"HI_TEST2","currency":{"code":"EUR"},"type":"front","values":{"2016-06-01":[{"asset":{"asset":1845,"quantity":1.0}}, {"asset": {"asset":2122,"quantity":1.0}}]}})
    port3 = json.dumps({"label":"HI_TEST3","currency":{"code":"EUR"},"type":"front","values":{"2016-06-01":[{"asset":{"asset":1845,"quantity":1.0}}, {"asset": {"asset":2122,"quantity":15.0}}]}})
    port4 = json.dumps({"label":"HI_TEST4","currency":{"code":"EUR"},"type":"front","values":{"2016-06-01":[{"asset":{"asset":1845,"quantity":1.0}}, {"asset": {"asset":2122,"quantity":14.0}}]}})
    port5 = json.dumps({"label":"HI_TEST5","currency":{"code":"EUR"},"type":"front","values":{"2016-06-01":[{"asset":{"asset":1845,"quantity":1.0}}, {"asset": {"asset":2122,"quantity":1.0}}]}})
    port6 = json.dumps({"label":"HI_TEST6","currency":{"code":"EUR"},"type":"front","values":{"2016-06-01":[{"asset":{"asset":1845,"quantity":1.0}}, {"asset": {"asset":2122,"quantity":2.0}}]}})
    port7 = json.dumps({"label":"HI_TEST7","currency":{"code":"EUR"},"type":"front","values":{"2016-06-01":[{"asset":{"asset":1845,"quantity":2.0}}, {"asset": {"asset":2122,"quantity":1.0}}]}})
    port8 = json.dumps({"label":"HI_TEST8","currency":{"code":"EUR"},"type":"front","values":{"2016-06-01":[{"asset":{"asset":1845,"quantity":10.0}}]}})
    port9 = json.dumps({"label":"HI_TEST9","currency":{"code":"EUR"},"type":"front","values":{"2016-06-01":[{"asset":{"asset":1845,"quantity":1.0}}, {"asset": {"asset":2122,"quantity":1.0}}, {"asset": {"asset":2156,"quantity":1.0}}, {"asset": {"asset":2128,"quantity":1.0}}, {"asset": {"asset":1429,"quantity":1.0}}, {"asset": {"asset":2063,"quantity":1.0}}, {"asset": {"asset":1858,"quantity":1.0}}, {"asset": {"asset":1881,"quantity":1.0}}, {"asset": {"asset":1891,"quantity":1.0}}, {"asset": {"asset":2072,"quantity":1.0}}, {"asset": {"asset":1913,"quantity":1.0}}, {"asset": {"asset":2164,"quantity":1.0}}]}})
                                                                                                             
    #2122,2156,2128,1429,2063,1858,1881,1891,2072,1913,2164
    non_actif = {'LAST_CLOSE_VALUE_IN_CURR': {'type': 'currency_value', 'value': '30,457 EUR'}, 'LABEL': {'type': 'string', 'value': '1818-VEGA EUR CO'}, 'TYPE': {'type': 'asset_type', 'value': 'FUND'}, 'ASSET_DATABASE_ID': {'type': 'int32', 'value': '2122'}}


    def test_enough_assets(self):
        port = prepare_portfolio(self)
        enough_assets(port)
        
    def test_unique_comp(self):
        port = prepare_portfolio(self)
        is_uniq_compo(port)
        
    def test_check_nav(self):
        port = prepare_portfolio(self)
        check_nav(port)
        
    def test_check_actions(self):
        port = prepare_portfolio(self)
        check_actions(port)


def prepare_portfolio(my_port):
    json_port = json.loads(my_port)
    #print(my_port)
    my_date = json_port['values'].keys()
    for elt in my_date:
        port = jsonToPortfolio(json_port, str(elt))
    return port

def safePortfolioTest_main():
    #------CHECK DATE-----
    SafePortfolioTests.test_unique_comp(SafePortfolioTests.port)
    SafePortfolioTests.test_unique_comp(SafePortfolioTests.port1)
    
    #------CHECK NUMBER ASSETS ------
    SafePortfolioTests.test_enough_assets(SafePortfolioTests.port2)
    SafePortfolioTests.test_enough_assets(SafePortfolioTests.port3)
    SafePortfolioTests.test_enough_assets(SafePortfolioTests.port4)

    #------CHECK NAV------
    SafePortfolioTests.test_check_nav(SafePortfolioTests.port1)
    SafePortfolioTests.test_check_nav(SafePortfolioTests.port2)    
    SafePortfolioTests.test_check_nav(SafePortfolioTests.our_port)
    SafePortfolioTests.test_check_nav(SafePortfolioTests.port8)
    SafePortfolioTests.test_check_nav(SafePortfolioTests.port9)

    #------CHECK ASSETS-----
    SafePortfolioTests.test_check_actions(SafePortfolioTests.port5)
    SafePortfolioTests.test_check_actions(SafePortfolioTests.port6)
    SafePortfolioTests.test_check_actions(SafePortfolioTests.port7)
    
if __name__ == '__main__':
    unittest.main()