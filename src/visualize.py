#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
font = fm.FontProperties(fname='/home/elaa2020/bigdata/hw/hw2/twitter_coronavirus/TTF/NanumSquareNeo-aLt.ttf')
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# stores count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
top_10 = items[:10]
sorted_top_10 = sorted(top_10, key=lambda item: item[1])
k, v = zip(*sorted_top_10)
title = args.key
x_label = args.input_path.split('.')[1].upper()

plt.bar(range(len(k)), v, tick_label=k)
plt.ylabel("Tweets")
plt.xlabel(x_label)
plt.title(f"Top 10 {x_label} with Tweets containing {title} in 2020", fontproperties = font)
plt.savefig(f"{x_label}_{title}.png")
