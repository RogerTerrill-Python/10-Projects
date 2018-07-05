import csv
import os
from data_types import Purchase
import statistics


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('--------------------------------------')
    print('    REAL ESTATE DATE MINING APP')
    print('--------------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:

        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases


# def get_price(p):
#     return p.price


def query_data(data):
    # data.sort(key=get_price)
    data.sort(key=lambda p: p.price)

    high_purchase = data[-1]
    print(f'The most expensive house is ${high_purchase.price:,} with {high_purchase.beds} beds and {high_purchase.baths} baths')

    low_purchase = data[0]
    print(f'The least expensive house is ${low_purchase.price:,} with {low_purchase.beds} beds and {low_purchase.baths} baths')

    prices = [
        p.price  # projections or items
        for p in data  # set to process
    ]

    avg_price = statistics.mean(prices)
    print(f'The average home price is ${int(avg_price):,}')

    two_bed_homes = [
        p  # projections or items
        for p in data  # set to process
        if p.beds == 2  # test/condition
    ]

    avg_price = statistics.mean([p.price for p in two_bed_homes])
    avg_baths = statistics.mean([p.baths for p in two_bed_homes])
    avg_sqft = statistics.mean([p.sq__ft for p in two_bed_homes])
    print(f'Average 2-bedroom home is ${int(avg_price):,}, baths={round(avg_baths,1)}, sqft={round(avg_sqft,1):,}')

if __name__ == '__main__':
    main()