import nltk
import sys

from os.path import join, abspath, dirname
apipath = abspath(join(dirname(__file__), ".."))
sys.path.append(apipath)

from db.connection import *

class Document():
    def __init__(self, title = "", uid = ""):
        self.title = title
        self.uid = uid
        self.text = ''

    def tokenize(self):
        self.__tokens__ = nltk.word_tokenize(self.text)

        return self.__tokens__

    def tokens(self):
        return self.__tokens__

    def save(self):
        result = True

        try:
            db = get_connection()
            self._id = db.documents.insert(self.__dict__)
        except:
            result = False

        return result
        
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

