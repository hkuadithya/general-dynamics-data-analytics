import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from  datetime import datetime
import os
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

_dataset2_dir = "C:/Users/talha/Documents/DA/da_project/dataset2/"
email_file = _dataset2_dir + "email_info.csv"
device_file = _dataset2_dir + "device_info.csv"
file_info = _dataset2_dir + "file_info.csv"

def get_polarity_and_subjectivity(text):
    blob = TextBlob(text)
    return pd.Series({"polarity": blob.sentiment.polarity, "subjectivity": blob.sentiment.subjectivity})

def vader_sentiment_analysis(text):
	 return analyzer.polarity_scores(text)['compound']

chunk_size = 100000
email_chunks = pd.read_csv(file_info, index_col=0, chunksize=chunk_size)

analyzer = SentimentIntensityAnalyzer()

# breakAt = 3
numChunks = 0
appended_data = []

for chunk in email_chunks:
	print ("\n ============ Processing chunk # "+ str(numChunks) +" =============\n")
	sentiment = chunk['content'].apply(vader_sentiment_analysis)
	appended_data.append(sentiment)
	print (sentiment.head())
	print (sentiment.shape)
	numChunks+=1
	# if numChunks == breakAt:
	# 	break

print ("\n ============ Processing Finished =============\n")
appended_data = pd.concat(appended_data, axis=0)
print (appended_data.head())
print (appended_data.shape)
print (type(appended_data))
appended_data.to_pickle(_dataset2_dir+"file_info_vader_sentiment_analysis_df")

print (numChunks)