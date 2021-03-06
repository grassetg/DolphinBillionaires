import json
import unittest
from models import DynAmountLineContainer as Container, DynAmountLineAsset as Asset, \
    DynAmountLineCurrency as Currency
from models import jsonToDynAmountLineAsset, jsonToDynAmountLineCurrency, \
    jsonToDynAmountLineContainer, createAssetContainer, createCurrencyContainer, Portfolio
from vars import PORTFOLIO_NAME


class PortfolioUnitTest(unittest.TestCase):
    def test_dynAmountLineContainer_happy_path(self):
        asset = Asset(2, 42.0)
        container = Container(asset, None)
        self.assertIsNotNone(container)
        self.assertEqual(container.asset, asset)

        currency = Currency(52.0)
        container2 = Container(None, currency)
        self.assertEqual(container2.currency, currency)

    def test_json_to_asset(self):
        jsonAsset = {
            "asset": 4920,
            "quantity": 1
        }

        asset = jsonToDynAmountLineAsset(jsonAsset)

        self.assertEqual(asset.asset, jsonAsset["asset"])
        self.assertEqual(asset.quantity, jsonAsset["quantity"])

        jsonAsString = json.dumps(jsonAsset)
        asset2 = jsonToDynAmountLineAsset(jsonAsString)

        self.assertEqual(asset.asset, asset2.asset)
        self.assertEqual(asset.quantity, asset2.quantity)

    def test_json_to_currency(self):
        jsonCurrency = {
            "amount": 500,
            "currency": "EUR"
        }

        currency = jsonToDynAmountLineCurrency(jsonCurrency)

        self.assertEqual(currency.amount, jsonCurrency["amount"])
        self.assertEqual(currency.currency, jsonCurrency["currency"])

        jsonAsString = json.dumps(jsonCurrency)
        currency2 = jsonToDynAmountLineCurrency(jsonAsString)

        self.assertEqual(currency.amount, currency2.amount)
        self.assertEqual(currency.currency, currency2.currency)

    def test_json_to_container_asset(self):
        jsonContainerAsset1 = {
            "asset": {
                "asset": 4920,
                "quantity": 1
            }
        }

        containerAsset = jsonToDynAmountLineContainer(jsonContainerAsset1)

        self.assertEqual(containerAsset.asset.asset, jsonContainerAsset1["asset"]["asset"])
        self.assertEqual(containerAsset.asset.quantity, jsonContainerAsset1["asset"]["quantity"])

        stringContainerAsset = json.dumps(jsonContainerAsset1)
        containerAsset2 = jsonToDynAmountLineContainer(stringContainerAsset)

        self.assertEqual(containerAsset.asset.asset, containerAsset2.asset.asset)
        self.assertEqual(containerAsset.asset.quantity, containerAsset2.asset.quantity)

    def test_json_to_container_currency(self):
        jsonContainerCurrency = {
            "currency": {
                "amount": 500,
                "currency": "€"
            }
        }

        containerCurrency1 = jsonToDynAmountLineContainer(jsonContainerCurrency)

        self.assertEqual(containerCurrency1.currency.amount, jsonContainerCurrency["currency"]["amount"])
        self.assertEqual(containerCurrency1.currency.currency, jsonContainerCurrency["currency"]["currency"])

        stringContainerCurrency = json.dumps(jsonContainerCurrency)
        containerCurrency2 = jsonToDynAmountLineContainer(stringContainerCurrency)

        self.assertEqual(containerCurrency1.currency.amount, containerCurrency2.currency.amount)
        self.assertEqual(containerCurrency1.currency.currency, containerCurrency2.currency.currency)

    def test_currency_container_to_json(self):
        currency = createCurrencyContainer(42.0)
        currencyDict = currency.toJson()

        # Dict test
        self.assertIsNotNone(currencyDict.get("currency", None))
        self.assertEqual(currencyDict["currency"].get("currency", None), "EUR")
        self.assertEqual(currencyDict["currency"].get("amount", None), 42.0)

    def test_asset_container_to_json(self):
        asset = createAssetContainer(2017, 1)
        assetDict = asset.toJson()

        # Dict test
        self.assertIsNotNone(assetDict.get("asset", None))
        self.assertEqual(assetDict["asset"].get("asset", None), 2017)
        self.assertEqual(assetDict["asset"].get("quantity", None), 1)

    def test_portfolio_to_json(self):
        currency1 = createCurrencyContainer(42.0)
        currency2 = createCurrencyContainer(2531.0)
        asset1 = createAssetContainer(2017, 5)
        asset2 = createAssetContainer(1760, 1)
        portfolio = Portfolio(PORTFOLIO_NAME, [asset1, currency1, asset2, currency2])
        portfolioDict = portfolio.toJson()

        self.assertEqual(portfolioDict.get("label", None), PORTFOLIO_NAME)
        self.assertIsNotNone(portfolioDict.get("currency", None))
        self.assertEqual(portfolioDict["currency"].get("code", None), "EUR")
        self.assertEqual(portfolioDict.get("type", None), "front")

        # values field
        self.assertIsNotNone(portfolioDict.get("values", None))
        self.assertIsNotNone(portfolioDict["values"].get("2016-06-01"))
        self.assertEqual(portfolioDict["values"]["2016-06-01"][0], asset1.toJson())
        self.assertEqual(portfolioDict["values"]["2016-06-01"][1], currency1.toJson())
        self.assertEqual(portfolioDict["values"]["2016-06-01"][2], asset2.toJson())
        self.assertEqual(portfolioDict["values"]["2016-06-01"][3], currency2.toJson())


if __name__ == '__main__':
    unittest.main()
