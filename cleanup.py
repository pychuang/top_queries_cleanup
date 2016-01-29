#!/usr/bin/env python

from __future__ import print_function

import argparse
import csv
import urllib


def cleanup(query):
    s = urllib.unquote_plus(query)
    s = ' '.join(s.split(','))
    s = ' '.join(s.split())
    s = s.lower()
    return s


def process(inputfile, outputfile, n):
    queries_set = set()
    queries = []
    with open(inputfile) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if n == 0:
                break
            query = cleanup(row[1])
            if query in queries_set:
                continue
            queries_set.add(query)
            queries.append(query)
            n -= 1

    with open(outputfile, 'w') as f:
        for query in queries:
            print(query, file=f)


def main():
    parser = argparse.ArgumentParser(description='Cleanup CiteSeerX top queries from Douglas')
    parser.add_argument('--input', required=True, help='specify input file')
    parser.add_argument('--output', required=True, help='specify output file')
    parser.add_argument('--top', help='number of queries for output')

    args = parser.parse_args()
    if args.top:
        n = int(args.top)
    else:
        n = -1
    process(args.input, args.output, n)


if __name__ == '__main__':
    main()
