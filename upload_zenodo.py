#!/usr/bin/env python
"""
inspired by https://github.com/darvasd/upload-to-zenodo/
"""
from argparse import ArgumentParser, Namespace
import pyzenodo3.upload as zup


def cmdparse() -> Namespace:
    p = ArgumentParser(description='Upload data to Zenodo staging')
    p.add_argument('apikey', help='Zenodo API key',
                   nargs='?')
    p.add_argument('inifn', help='mymeta.ini file with author, title, etc.')
    p.add_argument('path', help='directory or file to upload to Zenodo',
                   nargs='?')
    p.add_argument('-y', '--yes', help='upload to Zenodo, not just the sandbox',
                   action='store_true')
    return p.parse_args()


if __name__ == '__main__':
    p = cmdparse()

    metafn = zup.meta(p.inifn)
    zup.upload(metafn, p.path, p.apikey, p.yes)
