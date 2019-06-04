import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from queryer import Queryer
import platform
import json
import glob
import random


is_mac = platform.system() == 'Darwin'


class TestQueryer(unittest.TestCase):

    def test_dummy_data(self):
        queryer = Queryer()

    # @unittest.skipIf(not is_mac, "Use macOS to run this")
    # def test_NiTi(self):
    #     query = {
    #         'composition': 'Ni:1:1 Ti:2:2',
    #         'number_of_elements': '2'
    #     }
    #     ##query = {'icsd_collection_code': 181801}
    #     queryer = Queryer(query=query)
    #     parsed_entries = queryer.perform_icsd_query()
    #     print(parsed_entries)
    #     self.assertEqual(7, queryer.hits)
    #     queryer.quit()

    @unittest.skipIf(not is_mac, "Use macOS to run this")
    def test_AlOF(self):
        query = {
            'composition': 'Al O F',
            'number_of_elements': '3'
        }
        queryer = Queryer(query=query, structure_source='theory')
        queryer.perform_icsd_query()
        self.assertEqual(2, queryer.hits)

    @unittest.skipIf(not is_mac, "Use macOS to run this")
    def test_metadata(self):
        query = {
            "composition": "H:18:18 Al:6:6 O:28:28 P:4:4",
        }

        queryer = Queryer(query=query)
        queryer.perform_icsd_query()
        self.assertEqual(1, queryer.hits)

        with open("expected/5013/meta_data.json") as f:
            expected_dict = json.load(f)

        with open("5013/meta_data.json") as f:
            crawled_dict = json.load(f)

        # self.maxDiff = None
        # self.assertDictEqual(expected, crawled)

        assertion = True

        for key, expected in expected_dict.items():
            if key in crawled_dict.keys():
                if expected != crawled_dict[key]:
                    assertion = False
                    print(expected, crawled_dict[key])
            else:
                assertion = False
                print("Key {} is missing for the crawled data".format(key))

        assert assertion

    @unittest.skipIf(not is_mac, "Use macOS to run this")
    def test_cell_parameter(self):
        code = 251445
        query = {
            "icsd_collection_code": code,
        }

        queryer = Queryer(query=query)
        queryer.perform_icsd_query()
        self.assertEqual(1, queryer.hits)

        with open("expected/{}/meta_data.json".format(code)) as f:
            expected_dict = json.load(f)

        with open("{}/meta_data.json".format(code)) as f:
            crawled_dict = json.load(f)

        # self.maxDiff = None
        # self.assertDictEqual(expected, crawled)
        assertion = True

        for key, expected in expected_dict.items():
            if expected != crawled_dict[key]:
                assertion = False
                print(expected, crawled_dict[key])

        assert assertion

    @unittest.skipIf(not is_mac, "Use macOS to run this")
    def test_random(self):
        paths = glob.glob("expected/*")
        path = random.choice(paths)
        code = path.split("/")[-1]
        query = {
            "icsd_collection_code": code,
        }

        queryer = Queryer(query=query)
        queryer.perform_icsd_query()
        self.assertEqual(1, queryer.hits)

        with open("expected/{}/meta_data.json".format(code)) as f:
            expected_dict = json.load(f)

        with open("{}/meta_data.json".format(code)) as f:
            crawled_dict = json.load(f)

        # self.maxDiff = None
        # self.assertDictEqual(expected, crawled)
        assertion = True

        for key, expected in expected_dict.items():
            if expected != crawled_dict[key]:
                assertion = False
                print(expected, crawled_dict[key])

        assert assertion