import pandas
import os
import numpy as np

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models, similarities
from gensim.models import CoherenceModel, Phrases
from nltk.corpus import stopwords
from spacy.lang.en.stop_words import STOP_WORDS
import time



# Read data
print ("Reading data...")

_dataset2_dir = "C:/Users/talha/Documents/DA/da_project/dataset2/"
# # _dataset2_dir = "/groups/DataLightHouse/1004/DataSets2_10012017/"
email_file = _dataset2_dir + "email_info.csv"
data_email = pandas.read_csv(email_file)
doc_set = data_email["content"][:100].tolist()

print ("Read data complete")

# Stop Words.
tokenizer = RegexpTokenizer(r'\w+')
en_stop = set(get_stop_words('en'))
spacy_stop = set(STOP_WORDS)
nltk_stop = set(stopwords.words('english'))
my_stop_words = set(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'first', 'second', 'third',
                'many', 'however', 'since', 'either', 'although', 'much', 'also', 'another', 'became', 'become', 'usually', 
                    'also', 'c', 'along', 'made', 'still', 'known', 'took', 'less', 'around', 'though', 'part', 'gave',
                    'later', 'early', 'went', 'long', 'began', 'mid', 'set', 'late', 'wrote', 'given', 'day', 'away',
                    'able', 'way', 'met', 'come', 'etc', 'able', 'said', 'based', 'kept', 'left', 'came', 'led', 'old', 
                    'new', 'apart', 'named', 'agrees', 'received', 'left', 'found', 'begun', 'late', 'early',
                    'half', 'new', 'old', 'instead', 'despite', 'overall', 'b', 'including', 'f', 'eyes',
                     
                     'east', 'west', 'north', 'south', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 
                     'august', 'september', 'october', 'november', 'december', 'according', 
                     
                     'near', 'initial', 'ultimately', 'better'])

stop_words = en_stop.union(my_stop_words).union(nltk_stop).union(spacy_stop)

print("Total Stop words: " + str(len(stop_words)))


# Topic analysis using LDA.
def topic_analysis(data, num_topics, iterations=200):
    """
    @param data list of all the documents
    @param num_topics number of topics to find from topic modeling
    """
    texts = [None] * len(doc_set)
    # loop through document list
    for ind, i in enumerate(doc_set):
        # clean and tokenize document string
        raw = i.lower()
        tokens = tokenizer.tokenize(raw)
        # remove stop words from tokens
        stopped_tokens = [i for i in tokens if i not in stop_words and not i.isdigit()]
        # add tokens to list
        #texts.append(stopped_tokens)
        texts[ind]=stopped_tokens
    
    bigram = Phrases(texts)
    texts = [bigram[line] for line in texts]
        
    # remove words that appear only once
    all_tokens = sum(texts, [])
    tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
    texts = [[word for word in text if word not in tokens_once] for text in texts]

    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)
    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]
    ldamodel = models.ldamodel.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, 
                                        iterations=iterations, minimum_probability=0,
                                         passes=20) # , passes=20,  chunksize=10000
    return (ldamodel, dictionary, corpus, texts)


# Number of topics and iterations
iterations=100
num_topics = 10

# Doing Topic Analysis here.
print ("Starting topic analysis")
start_time = time.time()
print ("Start At: " + time.strftime("%H:%M:%S", time.gmtime(start_time)))

(ldamodel, dictionary, corpus, texts) = topic_analysis(doc_set, num_topics, iterations=iterations)

print ("LDA Model complete... " + 
	time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))

ldatopics = ldamodel.show_topics(formatted=False)
ldatopics = [[word for word, prob in topic] for topicid, topic in ldatopics]

# print ("Got ldatopics. Creating coherence model.. "  + 
# 	time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))

# Create Coherence Model
# CoherenceModel(topics=ldatopics, texts=texts, dictionary=dictionary).get_coherence() # , window_size=10

ldamodel.save("lda_model.model")
print ("Model saved as: lda_model.model")

# print (ldamodel.show_topics(formatted=False))

# To load the model later
#ldamodel_max_coherence =  models.LdaModel.load('ldamodel_max_coherence.model')

# Assign topics to emails:
# num_topics=10
# lda_corpus = [max(prob, key=lambda y:y[1])
#                     for prob in ldamodel[corpus] ]
# emails_LDA = [[] for i in range(num_topics)]
# for i, x in enumerate(lda_corpus):
#     emails_LDA[x[0]].append(doc_set[i])
