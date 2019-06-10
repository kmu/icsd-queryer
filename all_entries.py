import pandas as pd
import glob
from collection_coder import CollectionCoder
import time


class AllEntries():
    def __init__(self, first_code=0, n_codes=1000):
        self.cc = CollectionCoder(first_code, n_codes)

    def run(self):
        time.sleep(3)
        self.cc.q.wait_for_ajax()
        self.cc.q._check_list_view()
        self.cc.q._wait_until_dialogue_disappears()
        self.cc.q._click_select_all()
        self.cc.q._click_show_detailed_view()
        self.cc.q.parse_entries()

def main():
    # ae = AllEntries(50000)

    for i in range(1000):
        ae = AllEntries(i*1000+600000)
        ae.run()

if __name__ == '__main__':
    main()