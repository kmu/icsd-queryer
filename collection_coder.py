from queryer import Queryer
import pandas as pd
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


class CollectionCoder():
    def __init__(self):
        self.q = Queryer(structure_source="A")
        self.q.select_structure_source()
        self.q.driver.find_element_by_link_text("DB Info").click()

        self.previous_code = 0

    def run(self, first_code=1):
        last_code = first_code + 9999
        code_range = "{0}-{1}".format(first_code, last_code)

        textbox = self.q.driver.find_element_by_id("content_form:uiCodeCollection:input:input")
        textbox.send_keys(code_range)
        self.q._run_query()

        self.q._check_list_view()
        n_hits = self.q.hits
        n_pages = round(n_hits / 10)

        df_list = []

        for page in range(1, n_pages+1):

            self.q._wait_until_dialogue_disappears()
            self.q.wait_for_ajax()
            element = WebDriverWait(self.q.driver, 20).until(
                ec.presence_of_element_located((
                    By.CSS_SELECTOR, ".ui-icon-seek-next"
                )))
            # element.click()
            # self._save_csv(page, n_pages, code_range)
            _df = self._get_df()
            filename = "each/{0}-p{1}outof{2}ps.csv".format(code_range, page, n_pages)
            _df.to_csv(filename)

            df_list.append(_df)

            self.q.driver.execute_script("arguments[0].click();", element)
            # self.q.driver.find_element_by_css_selector(".ui-icon-seek-next").click()
            self.q._wait_until_dialogue_disappears()
            self.q.wait_for_ajax()

        combined_df = pd.concat(df_list)
        combined_df.to_csv("combined/comb_{}.csv".format(code_range))

    def _get_df(self):
        _df = self._get_current_df()
        while self.previous_code == _df['Coll. Code'].min():
            _df = self._get_current_df()
            time.sleep(0.1)

        self.previous_code = _df['Coll. Code'].min()
        print(_df)
        return(_df)

    def _get_current_df(self):
        table = self.q.get_html_table(idx=1)
        df = pd.read_html(table)[0]
        self.q.page_obatained = False  # Refresh
        return(df)

    # def _save_csv(self, page, n_pages, code_range):




def main():
    for i in range(100):
        cc = CollectionCoder()
        cc.run(i * 10000 + 1)

if __name__ == '__main__':
    main()
