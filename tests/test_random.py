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
        abolished_keys = ["misfit_layer"]
        new_keys = [
            'doi',
            "experimental_PDF_number",
            "is_structure_prototype",
            "cell_constants_without_sd",
            "calculated_PDF_number",
            "modulated_structure",
            "only_cell_and_structure_type",
            "temperature_factors_available"
        ]
        confclicting_keys = [
            'PDF_number',  #  2017 version returns 'R-value' by a bug
            "reference",
            'reference_1',  #  2017 version has uncleaned entry
            "comments"  #  Order of multiple comments can be different
        ]

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

        self.assertCountEqual(crawled_dict['comments'], expected_dict['comments'])

        for key in new_keys + confclicting_keys:
            del crawled_dict[key]

        for key in abolished_keys + confclicting_keys:
            del expected_dict[key]

        self.assertDictEqual(expected_dict, crawled_dict)
