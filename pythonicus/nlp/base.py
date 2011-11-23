import nltk

class Document():
    def __init__(self, title = "", uid = ""):
        self.__title__ = title
        self.__uid__ = uid

    # Setters and getters
    def set_text(self, text):
        self.__text__ = text

    def get_text(self):
        return self.__text__

    def get_uid(self):
        return self.__uid__

    def tokenize(self):
        self.__tokens__ = nltk.word_tokenize(self.__text__)

        return self.__tokens__

    def tokens(self):
        return self.__tokens__

    def save(self):
        result = True

        try:
            pass
        except:
            pass

        return result
        
    # Privates Methods
    def __checkword__(self,word):
        description = ""

        return description

def load_document(uid):
    return uid
