import urllib2
import csv
import logging
import argparse
import re
import datetime
import operator

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

    for row in csv_content:
        result = {"path": row[0], "date": row[1], "browser": row[2], "status": row[3], "size": row[4]}

        date = datetime.datetime.strptime(result["date"], date_results)
        times[date.hour] = times[date.hour] + 1

        hits += 1
        if re.search(r"\.(?:jpg|jpeg|gif|png)$", result["path"], re.I | re.M):
            imgHits += 1

        elif re.search("chrome/\d+", result["browser"], re.I):
            chrome += 1

        elif re.search("safari", result["browser"], re.I) and not re.search("chrome/\d+", result["browser"], re.I):
            safari += 1

        elif re.search("firefox", result["browser"], re.I):
            firefox += 1

        elif re.search("other", result["browser"], re.I):
            other += 1
    imageRequest = (float(imgHits) / hits) * 100
    browsers = {"Safari": safari, "Chrome": chrome, "Firefox": firefox, "OTHER": other}

    print "Results are as shown:"
    print "Image requests account for {0:0.1f}% of all requests.".format(imageRequest)
    print "The most popular browser is %s." % (max(browsers.iteritems(), key=operator.itemgetter(1))[0])

def main():
    parser = argparse.ArgumentParser(description='fetches the url')
    parser.add_argument('--info', '-u', '-url', help='tells you the url')
    args = parser.parse_args()
    _logger.info("Using URL = {}".format(args.info))

    data = Download(args.info)
