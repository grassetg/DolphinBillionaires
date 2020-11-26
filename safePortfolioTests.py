import json
import unittest
from safePortfolio import *
from models.portfolio import *

class SafePortfolioTests(unittest.TestCase):

    # Portfolios jsons
    jsonPort1 = {"label":"HI_TEST", "currency":{"code":"EUR"}, "type": "front", "values":{"2015-06-01":[{"asset":{"asset":1845,"quantity":1.0}}]}}
    jsonPort2 = {"label":"HI_TEST1", "currency":{"code":"EUR"}, "type": "front", "values":{"2016-06-01":[{"asset":{"asset":1845,"quantity":1.0}}]}}
    jsonPort3 = {"label":"HI_TEST2", "currency":{"code":"EUR"}, "type": "front", "values":{"2016-06-01":[{"asset":{"asset":1845,"quantity":1.0}}, {"asset": {"asset":2122,"quantity":1.0}}]}}
    jsonPort4 = {"label":"HI_TEST3", "currency":{"code":"EUR"}, "type": "front", "values":{"2016-06-01": [{"asset":{"asset":1845,"quantity":1.0}}, {"asset": {"asset":2122,"quantity":15.0}}]}}
    jsonPort5 = {"label":"HI_TEST4", "currency":{"code":"EUR"}, "type": "front", "values":{"2016-06-01": [{"asset":{"asset":1845,"quantity":1.0}}, {"asset": {"asset":2122,"quantity":14.0}}]}}
    jsonPort6 = {"label":"HI_TEST5","currency":{"code":"EUR"},"type":"front","values":{"2016-06-01":[{"asset":{"asset":1845,"quantity":1.0}}, {"asset": {"asset":2122,"quantity":1.0}}]}}
    jsonPort7 = {"label":"HI_TEST6","currency":{"code":"EUR"},"type":"front","values":{"2016-06-01":[{"asset":{"asset":1845,"quantity":1.0}}, {"asset": {"asset":2122,"quantity":2.0}}]}}
    jsonPort8 = {"label":"HI_TEST7","currency":{"code":"EUR"},"type":"front","values":{"2016-06-01":[{"asset":{"asset":1845,"quantity":2.0}}, {"asset": {"asset":2122,"quantity":1.0}}]}}
    jsonPort9 = {"label":"HI_TEST8","currency":{"code":"EUR"},"type":"front","values":{"2016-06-01":[{"asset":{"asset":1845,"quantity":10.0}}]}}
    jsonPort10 = {"label":"HI_TEST9","currency":{"code":"EUR"},"type":"front","values":{"2016-06-01":[{"asset":{"asset":1845,"quantity":1.0}}, {"asset": {"asset":2122,"quantity":1.0}}, {"asset": {"asset":2156,"quantity":1.0}}, {"asset": {"asset":2128,"quantity":1.0}}, {"asset": {"asset":1429,"quantity":1.0}}, {"asset": {"asset":2063,"quantity":1.0}}, {"asset": {"asset":1858,"quantity":1.0}}, {"asset": {"asset":1881,"quantity":1.0}}, {"asset": {"asset":1891,"quantity":1.0}}, {"asset": {"asset":2072,"quantity":1.0}}, {"asset": {"asset":1913,"quantity":1.0}}, {"asset": {"asset":2164,"quantity":1.0}}]}}

    # Porfolios objects
    port1 = jsonToPortfolio(jsonPort1, "2015-06-01")
    port2 = jsonToPortfolio(jsonPort2)
    port3 = jsonToPortfolio(jsonPort3)
    port4 = jsonToPortfolio(jsonPort4)
    port5 = jsonToPortfolio(jsonPort5)
    port6 = jsonToPortfolio(jsonPort6)
    port7 = jsonToPortfolio(jsonPort7)
    port8 = jsonToPortfolio(jsonPort8)
    port9 = jsonToPortfolio(jsonPort9)
    port10 = jsonToPortfolio(jsonPort10)

    #2122,2156,2128,1429,2063,1858,1881,1891,2072,1913,2164
    non_actif = {'LAST_CLOSE_VALUE_IN_CURR': {'type': 'currency_value', 'value': '30,457 EUR'}, 'LABEL': {'type': 'string', 'value': '1818-VEGA EUR CO'}, 'TYPE': {'type': 'asset_type', 'value': 'FUND'}, 'ASSET_DATABASE_ID': {'type': 'int32', 'value': '2122'}}


    def test_enough_assets(self):
        self.assertFalse(enough_assets(self.port3, False))
        self.assertFalse(enough_assets(self.port4, False))
        self.assertFalse(enough_assets(self.port5, False))

    def test_unique_comp(self):
        self.assertFalse(is_uniq_compo(self.port1, False))
        self.assertTrue(is_uniq_compo(self.port2, False))

    def test_check_nav(self):
        self.assertFalse(check_nav(self.port2, False))
        self.assertFalse(check_nav(self.port3, False))
        self.assertFalse(check_nav(self.port9, False))
        self.assertTrue(check_nav(self.port10, False))

    def test_check_actions(self):
        self.assertTrue(check_actions(self.port6, False))
        self.assertTrue(check_actions(self.port7, False))
        self.assertTrue(check_actions(self.port8, False))

if __name__ == '__main__':
    unittest.main()