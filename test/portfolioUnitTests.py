import json
import unittest
from models import DynAmountLineContainer as Container, DynAmountLineAsset as Asset, \
    DynAmountLineCurrency as Currency


class Test(unittest.TestCase):
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

        asset = Asset.jsonToDynAmountLineAsset(jsonAsset)

        self.assertEqual(asset.asset, jsonAsset["asset"])
        self.assertEqual(asset.quantity, jsonAsset["quantity"])

        jsonAsString = json.dumps(jsonAsset)
        asset2 = Asset.jsonToDynAmountLineAsset(jsonAsString)

        self.assertEqual(asset.asset, asset2.asset)
        self.assertEqual(asset.quantity, asset2.quantity)

    def test_json_to_currency(self):
        jsonCurrency = {
            "amount": 500,
            "currency": "EUR"
        }

        currency = Currency.jsonToDynAmountLineCurrency(jsonCurrency)

        self.assertEqual(currency.amount, jsonCurrency["amount"])
        self.assertEqual(currency.currency, jsonCurrency["currency"])

        jsonAsString = json.dumps(jsonCurrency)
        currency2 = Currency.jsonToDynAmountLineCurrency(jsonAsString)

        self.assertEqual(currency.amount, currency2.amount)
        self.assertEqual(currency.currency, currency2.currency)

    def test_json_to_container_asset(self):
        jsonContainerAsset1 = {
            "asset": {
                "asset": 4920,
                "quantity": 1
            }
        }

        containerAsset = Container.jsonToDynAmountLineContainer(jsonContainerAsset1)

        self.assertEqual(containerAsset.asset.asset, jsonContainerAsset1["asset"]["asset"])
        self.assertEqual(containerAsset.asset.quantity, jsonContainerAsset1["asset"]["quantity"])

        stringContainerAsset = json.dumps(jsonContainerAsset1)
        containerAsset2 = Container.jsonToDynAmountLineContainer(stringContainerAsset)

        self.assertEqual(containerAsset.asset.asset, containerAsset2.asset.asset)
        self.assertEqual(containerAsset.asset.quantity, containerAsset2.asset.quantity)

    def test_json_to_container_currency(self):
        jsonContainerCurrency = {
            "currency": {
                "amount": 500,
                "currency": "€"
            }
        }

        containerCurrency1 = Container.jsonToDynAmountLineContainer(jsonContainerCurrency)

        self.assertEqual(containerCurrency1.currency.amount, jsonContainerCurrency["currency"]["amount"])
        self.assertEqual(containerCurrency1.currency.currency, jsonContainerCurrency["currency"]["currency"])

        stringContainerCurrency = json.dumps(jsonContainerCurrency)
        containerCurrency2 = Container.jsonToDynAmountLineContainer(stringContainerCurrency)

        self.assertEqual(containerCurrency1.currency.amount, containerCurrency2.currency.amount)
        self.assertEqual(containerCurrency1.currency.currency, containerCurrency2.currency.currency)


if __name__ == '__main__':
    unittest.main()
