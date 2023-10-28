from generatingFinalFile.generatingFinalFile import GeneratingFinalFile
from parserFinancialExchangesBL.parserFinancialExchanges import ParserFinancialExchanges


def main():
    # Create an instance of the ParserFinancialExchanges class to fetch data from financial exchanges.
    parserFinancialExchanges = ParserFinancialExchanges()

    # Create an instance of the ParserFinancialExchanges class to fetch data from financial exchanges.
    all_name = parserFinancialExchanges.get_company_name()
    all_data=parserFinancialExchanges.get_all_data()

    # Create an instance of the GeneratingFinalFile class to create a file with the collected data.
    generatingFinalFile = GeneratingFinalFile()

    # Call the create_file() method to generate a file with the obtained data.
    generatingFinalFile.create_file(all_name, all_data)




if __name__ == '__main__':
    main()
