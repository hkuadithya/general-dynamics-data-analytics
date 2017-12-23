import pandas as pd
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

client = language.LanguageServiceClient()

alias_df = pd.read_pickle('../alias_df')

email_df = pd.read_pickle('../email_emp_df')

new_df = email_df[email_df['from'].isin(alias_df['suspicious_email_id'].values)]

del alias_df
del email_df

category = [None] * new_df.shape[0]
index = 0

for string in new_df['content_x']:
    try:
        if len(string) < 20:
            string = string + ' ' + string
        document = types.Document(content=string, type=enums.Document.Type.PLAIN_TEXT)
        categories = client.classify_text(document).categories
        category[index] = [c.name for c in categories]
    except:
        pass
    print(index)
    index += 1

new_df['category'] = category

print(new_df.head())

new_df.to_pickle('../new_email_emp_df')
