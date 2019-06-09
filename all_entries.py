import pandas as pd
import glob
from collection_coder import CollectionCoder


class AllEntries():
    def __init__(self, first_code=0, n_codes=1000):
        self.cc = CollectionCoder(first_code, n_codes)

    def run(self):
        self.cc.q._click_select_all()
        self.cc.q._click_show_detailed_view()
        self.cc.q.parse_entries()

def main():
    ae = AllEntries()
    ae.run()

if __name__ == '__main__':
    main()