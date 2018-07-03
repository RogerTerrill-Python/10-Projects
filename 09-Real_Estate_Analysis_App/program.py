import os


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    print(data)
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
    return []


def query_data(data):
    pass


if __name__ == '__main__':
    main()