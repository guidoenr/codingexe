import csv
from collections import Counter
from itertools import count

filename =  '2017.csv'
months = ["%.2d" % i for i in range(1,13)]
total = {
    "01":0, "02":0, "03":0,"04":0,"05":0,"06":0,"07":0,"08":0,"09":0,"10":0,"11":0,"12":0
}
trans = {
    "01":0, "02":0, "03":0,"04":0,"05":0,"06":0,"07":0,"08":0,"09":0,"10":0,"11":0,"12":0
}


def parse_dicts(total, trans):
    t = "Month: {}, Percentage: {}"
    for month in months:
        print(t.format(month, trans[month]/total[month] * 100))
        

if __name__ == '__main__':
    # What Exchange has had the most transactions in the file? 
    with open(filename, 'r') as f:
        column = (row['exchange'] for row in csv.DictReader(f) if row['exchange'] != 'off exchange')
        print("Most frequent value: {0}".format(Counter(column).most_common()[0][0]))

    # In August 2017, which companyName had the highest combined valueEUR?
    with open(filename, 'r') as f:
        column = (row for row in csv.DictReader(f) if row['inputdate'].startswith('2017'))
        m = max(column, key = lambda x: x['valueEUR'])
        print("Company name: {}, valueEUR: {}".format(m['companyName'], m['valueEUR']))

    # For 2017, only considering transactions with tradeSignificance 3, what is the percentage of transactions per month?
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for month in months:
                if row['tradeSignificance'] is '3' and row['inputdate'].startswith(f'2017{month}'):
                    total[month] += 1
                    trans[month] += 1 if row['exchange'] != 'off exchange' else 0
        parse_dicts(total, trans)

            