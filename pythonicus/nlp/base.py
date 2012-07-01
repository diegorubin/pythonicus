# coding: utf-8

import nltk
import string
import sys
from unicodedata import normalize

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
        text = self.remove_accents(self.text)
        tokens = nltk.word_tokenize(text)

        self.tokens = []
        stopwords = nltk.corpus.stopwords.words('portuguese')
        for w in tokens:
            if not ((w.lower() in stopwords) or (w in string.punctuation)):
                self.tokens.append(w)
                

        return self.tokens

    def stem(self):
        s = nltk.stem.RSLPStemmer()
        self.root_terms = []

        for token in self.tokens:
            self.root_terms.append(s.stem(token))

        return self.root_terms

    def remove_stopwords(self):
        text = self.remove_accents(self.text)
        tokens = nltk.word_tokenize(text)

        self.expressions = []
        expression = []
        stopwords = nltk.corpus.stopwords.words('portuguese')

        for w in tokens:

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

        self.tokenize()
        self.remove_stopwords()
        self.stem()

        result = True

        try:
            db = get_connection()
            if "_id" in dir(self):
                db.documents.update({'_id' : ObjectId(self._id)}, 
                                    {"$set" :{u'text' : self.text,
                                              u'expressions' : self.expressions,
                                              u'root_terms': self.root_terms,
                                              u'title': self.title,
                                              u'tokens': self.tokens}})
            else:
                self._id = db.documents.insert(self.__dict__)
        except:
            result = False

        return result

    def remove_accents(self,text):
        return normalize('NFKD', text.decode("utf-8")).encode('ASCII','ignore')

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
        d.__dict__["_id"] = uid
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

