# Generating main CSV file containing Unique URLs, count and content

from collections import Counter

import numpy as np
import pandas as pd

# Totally 28434424 Records
# fileLocation = 'C:/Users/hkuad/Desktop/Subjects/DA/DataSets/NewData/DataSet2/psychometric_info.csv'
# 6033 unique urls
# The output dataframe is sorted by the count

fileLocation = 'C:/Users/hkuad/Desktop/Subjects/DA/DataSets/NewData/DataSet2/http_info.csv'

urlContentDict = dict()
iteration = 1
counter = Counter()


def convertDF(counterDict):
    urls = list(urlContentDict.keys())
    contents = list(urlContentDict.values())
    counts = list(counterDict.values())

    df2 = pd.DataFrame(np.column_stack([contents, counts]), columns=['content', 'count'], index=urls)
    df2['count'] = df2['count'].astype(int)
    df2.index.name = 'url'
    df2.sort_values('count', ascending=False, inplace=True)
    df2.to_csv('url_count_content_descending.csv')


for df in pd.read_csv(fileLocation, sep=',', usecols=[4, 5], chunksize=1000000):
    counter.update(df['url'].values)
    urlContentDict.update(zip(df['url'], df['content']))
    print(iteration)
    iteration += 1

convertDF(counter)

print(len(counter))

print(counter.most_common(20))

# df = pd.read_csv(fileLocation, sep=',', usecols=[4, 5])
#
# print(len(df['url']), ' ', len(df['content']))
