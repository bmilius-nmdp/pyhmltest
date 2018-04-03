#!/usr/bin/env python3
"""
pyhmltest.py
plyaing with the pyHML package
"""


import pyhml


def main():
    """
    the main event
    """
    hml_file = 'C1PAC092116LRRABC_2016-09-28-111420.HML'
    hmlparser = pyhml.HmlParser()
    hml = hmlparser.parse(hml_file)
    # hml_df = pyhml.toDF(hml)
    outdir = 'output'

    # Print out each subject in fasta format
    pyhml.tobiotype(hml, outdir, dtype='fasta', by='subject')

    # Print out the full HML file in IMGT dat file format
    pyhml.tobiotype(hml, outdir, dtype='imgt', by='hml')

    # Get pandas DF from HML object
    pandasdf = pyhml.toDF(hml)
    print(pandasdf)


if __name__ == '__main__':
    main()
