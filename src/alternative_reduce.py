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
import matplotlib.dates as mdate
from matplotlib.ticker import MultipleLocator
from collections import Counter,defaultdict
from datetime import datetime

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
fig, ax = plt.subplots()
for hsh in args.hashtags:
    dates = []
    counts = []

    for k in total:
        if k[1] == hsh:
            dates.append(k[0])
            counts.append(total[k])

    dates_list = [datetime.strptime(date_str, "%y-%m-%d") for date_str in dates]
    ax.plot(dates_list, counts, label=hsh)

ax.xaxis.set_major_locator(mdate.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdate.DateFormatter("%y-%m-%d"))

plt.xlabel('Date')
plt.ylabel('Tweets')
plt.title('Daily tweets for provided hashtags')
plt.legend()

finalHashes = ""
for hsh in args.hashtags:
    finalHashes += hsh

plt.savefig(f'line_graph_{finalHashes}.png')
