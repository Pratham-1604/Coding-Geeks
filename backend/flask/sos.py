# -*- coding: utf-8 -*-
"""SOS

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hpg_y_7-svUJksRdpluuQntN5OFiMW_w

# Natural Language Processing

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv("distress_det.csv")

"""## Cleaning the texts"""

import re
import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []
for i in range(0, 40):
    review = re.sub("[^a-zA-Z]", " ", dataset["sentences"][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words("english")
    all_stopwords.remove("not")
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = " ".join(review)
    corpus.append(review)

# print(dataset['sentences'])
print(corpus)

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, -1].values

"""## Creating the Bag of Words model"""

from sklearn.naive_bayes import GaussianNB

classifier = GaussianNB()
classifier.fit(X, y)

"""## Splitting the dataset into the Training set and Test set"""

X_input = (
    "im travellling in the bus from A to B and i feel uncomfortable and unsafe. alpha "
)
safeword = "alpha"
# X_input='is this seat free. and also when is the next alpha metro'


def isSos(X_input, safeword):

    cor = []
    rev = re.sub("[^a-zA-Z]", " ", X_input)
    rev = rev.lower()
    rev = rev.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words("english")
    all_stopwords.remove("not")
    rev = [ps.stem(word) for word in rev if not word in set(all_stopwords)]
    rev = " ".join(rev)
    cor.append(rev)
    XX = cv.transform(cor).toarray()
    final = classifier.predict(XX)
    # if (final==1):
    #   print('Distress')
    # else:
    #   print('Allgood')
    if final == 1 and safeword in X_input:
        return "SOS"
    else:
        return "Allgood"


"""## Training the Naive Bayes model on the Training set"""


"""## Predicting the Test set results"""

# y_pred = classifier.predict(X_test)
# print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

"""## Making the Confusion Matrix"""

# from sklearn.metrics import confusion_matrix, accuracy_score
# cm = confusion_matrix(y_test, y_pred)
# print(cm)
# accuracy_score(y_test, y_pred)

# test="im travelling in the bus from A to B and i dont feel safe"
# test_pass = cv.transform([test])
# y_pred=classifier.predict(test_pass)
