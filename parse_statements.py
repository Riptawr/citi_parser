__author__ = 'riptawr'

import os
import sys
import pandas as pd


def get_statements(dir):
    """
    :param dir: folder to look for statements in
    :return: a list with found statements
    """
    statements = []
    os.chdir(dir)
    for i in os.listdir('.'):
        if i.startswith('ACCT'):
            statements.append(i)
    return statements


def accum(d, key):
    """
    :param key: the source name (a col in the dataframe)
    :return: sum of transactions for the key
    """
    return key, d['amount'][d['source'] == key].sum()


def get_stats(d, data_pair):
    """

    :param data_pair: a tuple of (source_name, amount_sum)
    :return: the summary statistics
    """
    return d['amount'][d['source'] == data_pair[0]].describe()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Finds Citibank statements in csv format and prints top transactions in 'source >> amount' format"
        print "Usage: parse_statements.py </dir/to/statment_csvs> <currency>'"
        sys.exit()

    statements_location = sys.argv[1]
    currency = sys.argv[2]

    names = ['date', 'source', 'amount', 'acc_number']

    d = pd.concat([pd.read_csv(f, header=None, names=names, encoding='utf-8-sig') for f in get_statements(statements_location)],
                  keys=get_statements(statements_location))

    # clean data from strings that have extra quotes at start and finish (only issues i found so far)
    for i in d['date'][d['date'].str.startswith('"')]:
        d['date'][d['date'] == i] = i[1:-1]

    # convert to datetime
    d['date'] = pd.to_datetime(d['date'], format='%d/%m/%Y')

    d.set_index(['date'], inplace=True)

    source_amount_pairs = []
    for i in d['source'].unique():
        source_amount_pairs.append(accum(d, i))

    sorted_stuff = sorted(source_amount_pairs, key=lambda x: x[1])

    print "\n"
    print "----------------------------------------------------------------------------------------------"
    print "- Top source >> withdraw amount "
    for i in sorted_stuff:
        print i[0], " #### ",  i[1], " ", currency
