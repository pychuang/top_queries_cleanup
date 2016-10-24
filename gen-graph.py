#!/usr/bin/env python

import argparse
import csv
import matplotlib.pyplot as plt
import sys


def process(args):
    if args.infile:
        inf = open(args.infile)
    else:
        inf = sys.stdin

    frequencies = []
    csvreader = csv.reader(inf)
    for row in csvreader:
        count, _ = row
        frequencies.append(int(count))

    frequencies.sort(reverse=True)
    print(frequencies)

    plt.plot(frequencies, 'r-', label='Query frequencies')
    plt.xlabel('Queries')
    plt.ylabel('Frequencies')
    plt.legend()
    plt.savefig('qf.png')
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Geneate graphs of top queries from Douglas')
    parser.add_argument('-i', '--infile', required=True, help='Input CSV file')

    args = parser.parse_args()
    process(args)


if __name__ == '__main__':
    main()
