import os
from collections import Counter

import pandas as pd
from gensim import corpora
from gensim.models.ldamodel import LdaModel

lda_model_file = 'url_lda_model.model'


def pre_process_data():
    fileLocation = 'C:/Users/hkuad/Desktop/Subjects/DA/Project/data-analytics-project/url-sentiment-analysis/url_count_content_descending.csv'

    df = pd.read_csv(fileLocation, sep=',', usecols=[1])

    counter = Counter()

    corpus = df['content']

    iteration = 0
    frequent_words = {'for', 'a', 'of', 'the', 'and', 'to', 'in'}

    for sentence in corpus:
        sub_list = sentence.lower().split(' ')
        for word in sub_list:
            if word in frequent_words:
                sub_list.remove(word)

        corpus[iteration] = sub_list
        counter.update(sub_list)
        iteration += 1

    for sentence in corpus:
        for word in sentence:
            if counter.get(word) < 2:
                sentence.remove(word)

    return corpus


def generate_lda_model():
    corpus = pre_process_data()

    dictionary = corpora.Dictionary(corpus)

    bow_corpus = [dictionary.doc2bow(text) for text in corpus]

    model = LdaModel(bow_corpus, num_topics=10, id2word=dictionary, passes=3)

    model.save(lda_model_file)

    return model


# if trained model is already available, use it else generate it...
if os.path.exists(lda_model_file):
    lda_model = LdaModel.load(lda_model_file)
else:
    lda_model = generate_lda_model()

print(lda_model.show_topics(formatted=False))

