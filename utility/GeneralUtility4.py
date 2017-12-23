# To find Most visited URL categories

import pandas as pd
from pprint import pprint
from collections import Counter
from ast import literal_eval
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

file = 'C:/Users/hkuad/Desktop/Subjects/DA/DataSets/NewData/DataSet2/http_info.csv'

url_category = '../url-sentiment-analysis/url_category_hits_count.csv'


def generate_url_category_hits():
    http_df = pd.read_csv(file, usecols=[4])

    url_df = pd.read_csv('../url-sentiment-analysis/url_google_sentiment_analysis.csv', usecols=[0, 5])

    url_df['category'] = url_df['category'].apply(literal_eval)

    url_df = pd.merge(http_df, url_df, on='url')['category']

    print(url_df)

    c = Counter()

    for row in url_df:
        c.update(row)

    pprint(c)

    df = pd.DataFrame.from_dict(c, orient='index').reset_index()

    df = df.rename(columns={'index': 'category', 0: 'count'})

    df.sort_values('count', ascending=False, inplace=True)

    df.reset_index(inplace=True, drop=True)

    df.to_csv(url_category, index=False)

    return df


if os.path.exists(url_category):
    url_cat_df = pd.read_csv(url_category, sep=',')
else:
    url_cat_df = generate_url_category_hits()

print(url_cat_df)

cat_dict = {'Food & Drink': 0, 'Beauty & Fitness': 0, 'Law & Government': 0, 'Sports': 0, 'Reference': 0,
            'Real Estate': 0, 'Games': 0, 'Science': 0, 'Hobbies & Leisure': 0, 'Business & Industrial': 0,
            'Autos & Vehicles': 0, 'Travel': 0, 'Home & Garden': 0, 'Shopping': 0, 'News': 0, 'Internet & Telecom': 0,
            'Online Communities': 0, 'People & Society': 0, 'Finance': 0, 'Pets & Animals': 0, 'Health': 0,
            'Books & Literature': 0, 'Computers & Electronics': 0, 'Arts & Entertainment': 0, 'Jobs & Education': 0,
            'Adult': 0}

for i in range(0, url_cat_df.shape[0]):
    for key in cat_dict.keys():
        if key in url_cat_df['category'][i]:
            cat_dict[key] += url_cat_df['count'][i]
            print(key, ' ', url_cat_df['category'][i])

pprint(cat_dict)

cat_dict = dict((k, v) for k, v in cat_dict.items() if v > 0)

pprint(cat_dict)

plt.gca().axis("equal")
labels = cat_dict.keys()

pie = plt.pie([float(v) for v in cat_dict.values()],
              startangle=0)

plt.legend(pie[0], labels, bbox_to_anchor=(1, 0.5),
           loc="center right", fontsize=10,
           bbox_transform=plt.gcf().transFigure)

plt.subplots_adjust(left=0.0, bottom=0.1, right=0.7)

plt.pie([float(v) for v in cat_dict.values()], labels=cat_dict.keys(), autopct=None)

plt.show()

plt.figure(0)

plt.bar(range(len(cat_dict)), cat_dict.values(), align='center')
plt.xticks(range(len(cat_dict)), cat_dict.keys(), rotation=90)
plt.gcf().subplots_adjust(bottom=0.3)

plt.show()
