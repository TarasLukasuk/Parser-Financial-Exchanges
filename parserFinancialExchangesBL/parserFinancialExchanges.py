import requests
from bs4 import BeautifulSoup
from toolz import partition

# This class is designed for parsing financial data of stock names on United States exchanges.


class ParserFinancialExchanges:
    # The URL of the web page we'll be parsing.
    __url = "https://ru.investing.com/equities/united-states"
    # Headers used for the HTTP request.
    __header = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.188 Safari/537.36"
    }
    # Perform an HTTP request to get the page content and parse it using BeautifulSoup.
    __request = requests.get(__url, __header)
    __soup = BeautifulSoup(__request.text, "lxml")

    # Method to get the names of the companies from the page.
    def get_company_name(self):
        all_name = self.__soup.find_all(class_="pt-2 font-normal dynamic-table_cell-symbol__iswqe")
        list_name = []

        for item_name in all_name:
            if item_name is not None:
                list_name.append(item_name.text)
        return list_name

    # Method to get all the financial data about the companies on the page and split them into groups of 5.
    def get_all_data(self):
        all_data = self.__soup.find_all(class_="datatable_cell__LJp3C datatable_cell--align-end__qgxDQ dynamic-table_col-other__Eu_RC")
        list_data = []

        for item_last in all_data:
            list_data.append(item_last.text)

        result = list(partition(5, list_data))
        return result