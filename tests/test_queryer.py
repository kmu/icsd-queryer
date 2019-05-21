import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from queryer import Queryer
import unittest


class TestQueryer(unittest.TestCase):
    def test_NiTi(self):
        query = {
            'composition': 'Ni:1:1 Ti:2:2',
            'number_of_elements': '2'
        }
        ##query = {'icsd_collection_code': 181801}
        queryer = Queryer(query=query)
        queryer.perform_icsd_query()
        # print queryer.hits
        # queryer.quit()
