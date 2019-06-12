import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from crawler import Crawler

class TestCrawl(unittest.TestCase):
    def test_number_range(self):
        crawler = Crawler()
        crawler.crawled_codes = [60, 61, 100, 103, 105]
        self.assertEqual("0-59", crawler.get_code_range())

        crawler.crawled_codes = [100, 103, 105] + list(range(62))
        self.assertEqual("62-99", crawler.get_code_range())

        crawler.crawled_codes = [100, 103, 105] + list(range(100))
        self.assertEqual("101-102", crawler.get_code_range())