from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import multiprocessing as mp
import pandas as pd
import os
import time

employee_df_file = 'C:/Users/hkuad/Desktop/Subjects/DA/Project/data-analytics-project/emp_df'

email_csv_file = 'C:/Users/hkuad/Desktop/Subjects/DA/DataSets/NewData/DataSet2/email_info.csv'

it_admin_email_content = 'it_admin_email_content.csv'

it_admin_email_category = 'it_admin_email_category.csv'

it_admin = 'ITAdmin'

client = language.LanguageServiceClient()


def generate_email_df():
    it_admin_employees = pd.read_pickle(employee_df_file)

    it_admin_employees = it_admin_employees.loc[it_admin_employees['role'] == it_admin]['user_id'].values

    # 0     1   2      3   4   5   6    7      8        9              10
    # id, date, user, pc, to, cc, bcc, from, size, attachment_count, content
    temp_email_df = pd.read_csv(email_csv_file, sep=',', usecols=[0, 2, 10])

    temp_email_df = temp_email_df.loc[temp_email_df['user'].isin(it_admin_employees)]

    temp_email_df.to_csv(it_admin_email_content, index=False)

    return temp_email_df


def processInput(string):
    time.sleep(0.105)
    try:
        if len(string) < 20:
            string += string
        document = types.Document(content=string, type=enums.Document.Type.PLAIN_TEXT)
        categories = client.classify_text(document).categories
        # print(categories)
        return [c.name for c in categories]
    except:
        return None

if __name__ == '__main__':

    if os.path.exists(it_admin_email_content):
        email_df = pd.read_csv(it_admin_email_content, sep=',')
    else:
        email_df = generate_email_df()

    start = time.time()
    output = mp.Pool(2).map(processInput, email_df['content'])
    print(time.time() - start)

    email_df.drop(['user', 'content'], axis=1, inplace=True)

    email_df['category'] = output

    email_df.to_csv(it_admin_email_category, index=False)

    os.system('shutdown /h')
