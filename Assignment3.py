from __future__ import print_function, division

import urllib2
import csv
import logging
import argparse
import re
import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
_logger = logging.getLogger('assignment3')

URL = "http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv"
def Download(info):
    ans = urllib2.urlopen(info)
    return ans.read()


def csv_data(content):
    csv_content = csv.reader(content)
    date_results = "%Y-%m-%d %H:%M:%S"
    hits = 0
    imgHits = 0
    safari = 0
    chrome = 0
    firefox = 0
    other = 0
    times = {i: 0 for i in range(0, 24)}
    for row in csv_data:
        result = {"path": row[0], "date": row[1], "browser": row[2], "status": row[3], "size": row[4]}

        date = datetime.datetime.strptime(result["date"], date_results)
        times[date.hour] = times[date.hour] + 1


def main():
    parser = argparse.ArgumentParser(description='fetches the url')
    parser.add_argument('--info', '-u', '-url', help='tells you the url')
    args = parser.parse_args()
    _logger.info("Using URL = {}".format(args.info))
