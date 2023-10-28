class GeneratingFinalFile:
    # Method to create a file with company names and their financial data.
    def create_file(self, all_company_name, all_company_data):

        unique_company_names = set()  # Create a set to track unique company names.

        with open("data.txt", "a", encoding="utf-8") as file:
            # Iterate over the pairs of company names and their data.
            for item_company_name, item_company_data in zip(all_company_name, all_company_data):
                if item_company_name not in unique_company_names:
                    # Write company name, last price, maximum, minimum, and volume to the file.
                    file.write(f"Назва:{item_company_name} "
                               f"Послед: {item_company_data[0]} "
                               f"Макс: {item_company_data[1]} "
                               f"Мин: {item_company_data[2]} "
                               f"Объём: {item_company_data[3]}\n")
                    unique_company_names.add(item_company_name)  # Add the name to the set to track uniqueness.
