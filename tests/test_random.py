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


class TestRandom(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

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

        self.assertDictEqual(expected_dict, crawled_dict)

        for key, expected in expected_dict.items():
            if expected != crawled_dict[key]:
                assertion = False
                print("=======================")
                print("Mismatch in {}".format(key))
                print(expected, crawled_dict[key])

        # assert assertion
        self.assertDictEqual(expected_dict, crawled_dict)
