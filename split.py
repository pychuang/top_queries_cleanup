#!/usr/bin/env python

import argparse
import os

def process(inputpath):
    (head, tail) = os.path.splitext(inputpath)
    outputpath1 = head + '.even' + tail
    outputpath2 = head + '.odd' + tail
    inputfile = open(inputpath, 'r')
    outputfile1 = open(outputpath1, 'w')
    outputfile2 = open(outputpath2, 'w')
    even = True
    while True:
        line = inputfile.readline()
        if not line:
            break
        if even:
            outputfile1.write(line)
            even = False
        else:
            outputfile2.write(line)
            even = True

def main():
    parser = argparse.ArgumentParser(description='Cleanup CiteSeerX top queries from Douglas')
    parser.add_argument('inputfile', help='specify input file')

    args = parser.parse_args()
    process(args.inputfile)


if __name__ == '__main__':
    main()
