from icsd.collection_coder import CollectionCoder
from tqdm import tqdm
import time
from icsd import queryer
import os


def main():
    for i in tqdm(range(10)):
        try:
            tt = CollectionCoder(i * 100000 + 1, i * 100000 + 100000)

            tt.combined_csv_path = "combined_theory/comb_{}.csv".format(tt.code_range)
            tt.each_path = "each_theory"
            tt.structure_source = "T"

            print(tt.combined_csv_path)
            if not os.path.exists(tt.combined_csv_path):
                tt.run()
        except queryer.QueryerError:
            with open(tt.combined_csv_path, "w") as f:
                f.write("")

            print("No entry found in this step")
            tt.quit()
            time.sleep(5)


if __name__ == '__main__':
    main()
