import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)'
simpsons = pd.read_html(url)

# Create a Pandas Excel writer using XlsxWriter as the engine
writer = pd.ExcelWriter('scrapedSimpsons.xlsx', engine='xlsxwriter')

# Iterate over each table and write it to a separate sheet in the Excel file
for i, table in enumerate(simpsons):
    table_name = f"Table{i+1}"  # Generate a unique sheet name
    # Select all columns except the first column (column 'A')
    table.iloc[:, 1:].to_excel(writer, sheet_name=table_name, index=True)

# Save and close the Excel writer
writer.close()
