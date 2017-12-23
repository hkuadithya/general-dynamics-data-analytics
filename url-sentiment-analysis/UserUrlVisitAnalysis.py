import pandas as pd
import numpy as np
import os
import seaborn as sns

# Global Variables
neg_thresh = -0.2

pos_thresh = 0.1

http_info_file = 'C:/Users/hkuad/Desktop/Subjects/DA/DataSets/NewData/DataSet2/http_info.csv'

url_sentiment_file = 'url_google_sentiment_analysis.csv'

user_url_sentiment_csv = 'url_user_google_visit_pattern_analysis.csv'

psychometric_analysis_file = 'C:/Users/hkuad/Desktop/Subjects/DA/DataSets/NewData/DataSet2/psychometric_info.csv'

url_user_google_psychometric_analysis = 'url_user_google_psychometric_analysis.csv'


def generate_url_user_sentiment_list():
    url_df = pd.read_csv(url_sentiment_file, sep=',', usecols=[0, 3])

    df = pd.read_csv(http_info_file, sep=',', usecols=[2, 4])

    merged = pd.merge(df, url_df, on='url')

    del df

    pos = merged[merged['sentiment'] > pos_thresh].groupby('user').agg({'url': np.size, 'sentiment': np.mean})
    pos.rename(columns={'url': 'pos_count', 'sentiment': 'pos_mean'}, inplace=True)

    neg = merged[merged['sentiment'] < neg_thresh].groupby('user').agg({'url': np.size, 'sentiment': np.mean})
    neg.rename(columns={'url': 'neg_count', 'sentiment': 'neg_mean'}, inplace=True)

    neutral = merged[(merged['sentiment'] >= neg_thresh) & (merged['sentiment'] <= pos_thresh)] \
        .groupby('user').agg({'url': np.size, 'sentiment': np.mean})
    neutral.rename(columns={'url': 'neutral_count', 'sentiment': 'neutral_mean'}, inplace=True)

    del merged

    temp = pd.concat([pos, neg, neutral], axis=1)

    temp.fillna(0, inplace=True)

    temp['pos_count'] = temp['pos_count'].astype(int)
    temp['neg_count'] = temp['neg_count'].astype(int)
    temp['neutral_count'] = temp['neutral_count'].astype(int)

    temp.index.rename('user_id', inplace=True)
    temp.reset_index(inplace=True)

    temp.to_csv(user_url_sentiment_csv, index=False)

    return temp


def publish_psychometric_url_visit_pattern():
    psychometric_df = pd.read_csv(psychometric_analysis_file, sep=',')

    psychometric_df = pd.merge(psychometric_df, user_df, on='user_id')

    psychometric_df.to_csv(url_user_google_psychometric_analysis, index=False)


# Entry point for execution of main program
if os.path.exists(user_url_sentiment_csv):
    user_df = pd.read_csv(user_url_sentiment_csv, sep=',')
else:
    user_df = generate_url_user_sentiment_list()

publish_psychometric_url_visit_pattern()
