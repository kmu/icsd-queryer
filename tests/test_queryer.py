import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from queryer import Queryer
import platform


is_mac = platform.system() == 'Darwin'


class TestQueryer(unittest.TestCase):
    @unittest.skipIf(not is_mac, "Use macOS to run this")
    def test_NiTi(self):
        query = {
            'composition': 'Ni:1:1 Ti:2:2',
            'number_of_elements': '2'
        }
        ##query = {'icsd_collection_code': 181801}
        queryer = Queryer(query=query)
        parsed_entries = queryer.perform_icsd_query()
        print(parsed_entries)
        self.assertEqual(7, queryer.hits)
        queryer.quit()



    @unittest.skipIf(not is_mac, "Use macOS to run this")
    def test_AlOF(self):
        query = {
            'composition': 'Al O F',
            'number_of_elements': '3'
        }
        queryer = Queryer(query=query, structure_source='theory')
        queryer.perform_icsd_query()
        self.assertEqual(3, queryer.hits)