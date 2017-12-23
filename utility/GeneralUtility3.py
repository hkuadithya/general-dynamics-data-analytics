import pandas as pd
from pprint import pprint

user_job_url_df = pd.read_pickle('../url-sentiment-analysis/user_job_url_hits.pickle')

emp_df = pd.read_pickle('../emp_df')

emp_df = emp_df.loc[(emp_df['user_id'].isin(user_job_url_df.index)) & (emp_df['left'] == 1)]

emp_df = emp_df['user_id']
pprint(len(emp_df.values))

pprint(user_job_url_df)
