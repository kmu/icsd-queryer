import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from queryer import Queryer
import unittest

<<<<<<< HEAD


class TestQueryer(unittest.TestCase):
    def test_NiTi(self):
        query = {
            'composition': 'Ni:1:1 Ti:2:2',
            'number_of_elements': '2'
        }
        ##query = {'icsd_collection_code': 181801}
        queryer = Queryer(query=query)
        parsed_entries = queryer.perform_icsd_query()
        print(parsed_entries)
        print(queryer.hits)
        queryer.quit()
=======
query = {
    'composition': 'Al O F',
    'number_of_elements': '3'
    }
queryer = queryer.Queryer(query=query, structure_source='theory')
queryer.perform_icsd_query()
>>>>>>> hegdevinayi/master
