import nltk

class PersistedText():
    def __init__(self, text = ""):
        self.__text__ = text

    def tokenize(self):
        self.__tokens__ = nltk.word_tokenize(self.__text__)

        return self.__tokens__

    def tokens(self):
        return self.__tokens__

    def __checkword__(self,word):
        description = ""

        return description

