#!/usr/bin/env python3
import matplotlib.pyplot as mpl

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
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
#for k,v in items:
#    print(k,':',v)

#    sorted the top 10 items in the dictionary based on value
sorted_dict = sorted(items[0:10], key=lambda item: item[1], reverse=False)
#print("top_10", = sorted_dict)

#creating x and y values
x = range(len(sorted_dict))
y = [item[1] for item in sorted_dict]
label = [item[0] for item in sorted_dict]
print("x,y=", x,y)
mpl.bar(x,y)

mpl.xsticks(x,label)
mpl.xlabel("Country")
mpl.ylabel("Number of Tweets")
mpl.tile = ("Number of Coronavirus mentions")
mpl.show()
