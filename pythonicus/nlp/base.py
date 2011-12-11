# coding: utf-8

import nltk
import string
import sys

from os.path import join, abspath, dirname
apipath = abspath(join(dirname(__file__), ".."))
sys.path.append(apipath)

from db.connection import *

table = string.maketrans("","")

class Document():
    def __init__(self, title = ""):
        self.title = title
        self.text = ''

    def tokenize(self):
        self.tokens = nltk.word_tokenize(self.text)

        return self.tokens

    def remove_stopwords(self):
        self.expressions = []
        expression = []
        stopwords = nltk.corpus.stopwords.words('portuguese')

        for w in self.tokenize():

            if (w.lower() in stopwords) or (w in string.punctuation):
                w = w.translate(table, string.punctuation)
                
                if len(expression) > 0:
                    self.expressions.append(expression)
                    expression = []
            else:
                expression.append(w)

        if len(expression) > 0:
            self.expressions.append(expression)

        self.__normalize_expressions()

        return self.expressions


    def to_json(self):
        json = self.__dict__

        try:
            json['_id'] = str(json['_id'])
        except:
            json['_id'] = None

        return json

    def save(self):
        self.remove_stopwords()
        result = True

        try:
            db = get_connection()
            self._id = db.documents.insert(self.__dict__)
        except:
            result = False

        return result

    def __normalize_expressions(self):
        if self.expressions:
            self.expressions.sort()
            last = self.expressions[-1]

            for i in range(len(self.expressions)-2, -1, -1):
                if last == self.expressions[i]:
                    del self.expressions[i]
                else:
                    last = self.expressions[i]
        
def load_document(uid):

    d = Document()
    
    try:
        db = get_connection()
        obj = db.documents.find({"_id" : ObjectId(uid)})


        d.__dict__ = obj[0]
    except:
        pass

    return d

def all_documents(**kwargs):
    documents = []

    try:
        db = get_connection()
        docs = db.documents.find()

        for doc in docs:
            d = Document()
            d.__dict__ = doc

            documents.append(d)

    except:
        pass

    return documents

