from ast import literal_eval
from pprint import pprint
import pandas as pd
import numpy as np

user_job_url_hits_file = '../url-sentiment-analysis/user_job_url_hits.pickle'

job_flag = {'/Jobs & Education/Jobs', '/Jobs & Education/Jobs/Career Resources & Planning',
            '/Jobs & Education/Jobs/Job Listings', '/Jobs & Education/Jobs/Resumes & Portfolios'}

url_category = pd.read_csv('../url-sentiment-analysis/url_google_sentiment_analysis.csv', sep=',', usecols=[0, 5])

user_url_df = pd.read_csv('C:/Users/hkuad/Desktop/Subjects/DA/DataSets/NewData/DataSet2/http_info.csv', sep=',',
                          usecols=[2, 4])

url_category['category'] = url_category['category'].apply(literal_eval)

url_list = [None] * url_category.shape[0]

for i in range(0, url_category.shape[0]):
    for category in url_category['category'][i]:
        if category in job_flag:
            url_list[i] = url_category['url'][i]
            break

url_list = [url for url in url_list if url is not None]

pprint(url_list)

user_url_df = user_url_df[user_url_df['url'].isin(url_list)]

user_url_df = user_url_df.groupby('user').agg({'url': np.size})

user_url_df.rename(columns={'url': 'job_url_hits'}, inplace=True)

user_url_df.sort_values('job_url_hits', ascending=False, inplace=True)

user_url_df.to_pickle(user_job_url_hits_file)

pprint(user_url_df)
