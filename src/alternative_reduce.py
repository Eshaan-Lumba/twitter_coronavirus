#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--hashtags',nargs='+',required=True)
args = parser.parse_args()

# imports
import os
import json
import glob
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter,defaultdict

total = {}
file_pat = "/home/elaa2020/bigdata/hw/hw2/twitter_coronavirus/outputs/geoTwitter20-*.lang"
files = glob.glob(file_pat)
for file in files:
    with open(file) as f:
        date = os.path.basename(file)[10:18]
        tmp = json.load(f)
        for hsh in args.hashtags:
            if hsh in tmp:
                for language in tmp[hsh]:
                    if (date, hsh) not in total:
                        total[(date, hsh)] = 0
                    
                    total[(date, hsh)] += tmp[hsh][language]

total = dict(sorted(total.items(), key = lambda key: key[0]))
for hsh in args.hashtags:
    dates = []
    counts = []

    for k in total:
        if k[1] == hsh:
            dates.append(k[0])
            counts.append(total[k])

    plt.plot(dates, counts, label=hsh)

shownDates = ["20-02-01", "20-04-01", "20-06-01", "20-08-01", "20-10-01"]
plt.xticks(shownDates, rotation=45)
plt.xlabel('Date')
plt.ylabel('Tweets')
plt.title('Daily tweets for provided hashtags')
plt.legend()
plt.tight_layout()

plt.savefig(f'line_graph_{args.hashtags}.png')
