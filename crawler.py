import glob
import pandas as pd
import os
import math
from all_entries import AllEntries


class Crawler(object):
    def __init__(self):
        pass

    def get_code_range(self):
        def get_within_value(start, end):
            for c in self.crawled_codes:
                if start <= c and c <= end:
                    return(c)

            return(-1)

        start = self.not_yet_crawled[0]
        end = self.all_codes[self.all_codes.index(start) + 99]  # 100 is the maximum of DL

        within_val = get_within_value(start, end)

        if within_val > 0:
            end = within_val - 1

        return(start, end)

    def refresh(self):
        paths = glob.glob("combined/*.csv")
        df_list = []

        for p in paths:
            if os.stat(p).st_size > 0:
                _df = pd.read_csv(p)
                df_list.append(_df)

        cdf = pd.concat(df_list, ignore_index=True, sort=False)
        cdf.to_csv('all_coolection_code.csv')

        assert(cdf["Coll. Code"].duplicated() == True).sum() == 0

        print("{} structures are in Collection Code list".format(len(cdf)))

        cdf = cdf.sort_values(by=["Coll. Code"])
        # print(cdf)

        crawled = glob.glob("*/source.html")
        crawled = [int(c.split("/")[0]) for c in crawled]

        cdf2 = cdf[~cdf["Coll. Code"].isin(crawled)]
        print("{} structures are not retrieved".format(len(cdf2)))

        self.crawled_codes = sorted(crawled)
        self.all_codes = cdf["Coll. Code"].tolist()
        self.not_yet_crawled = cdf2["Coll. Code"].tolist()

    def run(self):
        self.refresh()


        while len(self.not_yet_crawled) > 0:
            start, end = self.get_code_range()

            ae = AllEntries(start, end)
            ae.run()

            self.refresh()

def main():
    c = Crawler()
    c.run()