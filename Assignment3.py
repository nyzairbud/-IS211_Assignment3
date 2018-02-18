from __future__ import print_function, division

import urllib2
import csv
import logging
import argparse

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
_logger = logging.getLogger('assignment3')

URL = "http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv"
def Download(info):
    ans = urllib2.urlopen(info)
    return ans.read()




def main():
    parser = argparse.ArgumentParser(description='fetches the url')
    parser.add_argument('--info', '-u', '-url', help='tells you the url')
    args = parser.parse_args()
    _logger.info("Using URL = {}".format(args.url))