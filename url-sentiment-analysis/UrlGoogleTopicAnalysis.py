# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import pandas as pd

# Instantiates a client
client = language.LanguageServiceClient()

df = pd.read_csv('url_count_content_descending.csv', sep=',')

sentiment = [None] * df.shape[0]
magnitude = [None] * df.shape[0]
category = [None] * df.shape[0]

index = 0
exception_count = 0

for row in df['content']:

    document = types.Document(content=row, type=enums.Document.Type.PLAIN_TEXT)

    try:
        s = client.analyze_sentiment(document=document).document_sentiment
        sentiment[index] = s.score
        magnitude[index] = s.magnitude

        categories = client.classify_text(document).categories
        category[index] = [c.name for c in categories]
    except:
        exception_count += 1

    index += 1
    print(index)

# url,content,count
df['sentiment'] = sentiment
df['magnitude'] = magnitude
df['category'] = category

df.sort_values(['sentiment', 'count'], ascending=[True, False], inplace=True)
df.reset_index(drop=True)
df.to_csv('url_google_sentiment_analysis.csv', index=False)

print('Unclassified URLs : ', exception_count)
