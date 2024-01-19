# Project name: Companies Data Visualization
# Author: Wellinton Oliveira Santos
# Location: Três Corações, MG, Brazil
# Year: 2023


from bs4 import BeautifulSoup
from tabulate import tabulate
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import requests
import pandas as pd


def main():
    x = get_data()
    print(table(x))

def get_data():
    url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find_all('table')[1]
    world_titles = table.find_all('th')

    world_table_titles = [title.text.strip() for title in world_titles]

    df = pd.DataFrame(columns = world_table_titles)

    column_data = table.find_all('tr')
    for row in column_data[1:]:
        row_data = row.find_all('td')
        individual_row_data = [data.text.strip() for data in row_data]

        length = len(df)
        df.loc[length] = individual_row_data

    df.to_csv(r'companies.csv', index = False)
    get_pdf(df)

    return df

def table(df):
    return tabulate(df, headers='keys', showindex=False)

def get_pdf(df):
    fig, ax =plt.subplots(figsize=(10,4))
    ax.axis('tight')
    ax.axis('off')

    cell_loc = 'center'

    the_table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', fontsize='large', cellLoc=cell_loc)
    pp = PdfPages("companies.pdf")
    pp.savefig(fig, bbox_inches='tight')
    pp.close()


if __name__ == '__main__':
    main()
