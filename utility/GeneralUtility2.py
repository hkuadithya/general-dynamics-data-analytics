from ast import literal_eval
import pandas as pd
from collections import Counter
import pprint

file = "../url-sentiment-analysis/url_google_sentiment_analysis.csv"

counter = Counter()

df = pd.read_csv(file, usecols=[5])

df['category'].fillna('', inplace=True)


for row in df['category']:
    if row is not None:
        row = literal_eval(row)
        counter.update(row)


pprint.pprint(counter.most_common())
