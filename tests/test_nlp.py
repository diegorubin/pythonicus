# coding: utf-8

import unittest

try:
    from pythonicus.nlp.base import *
except ImportError:
    import sys
    from os.path import join, abspath, dirname
    parentpath = abspath(join(dirname(__file__), '..'))
    sys.path.append(parentpath)
    from pythonicus.nlp.base import *


class test_base(unittest.TestCase):

    def test_tokenize_string(self):
        doc = Document("apenas um teste")
        doc.text = "apenas um teste"
        tokens = doc.tokenize()
        self.assertEqual(len(tokens),2)

    def test_remove_stopwors(self):
        doc = Document("frase")
        doc.text = "Um Arduino para Diego"
        expressions = doc.remove_stopwords()

        self.assertTrue(['Arduino'] in expressions)
        self.assertTrue(['Diego'] in expressions)

    def test_remove_punctuation(self):
        doc = Document("outro teste")
        doc.text = "Olho, Orelha."
        expressions = doc.remove_stopwords()

        self.assertTrue(['Olho'] in expressions)
        self.assertTrue(['Orelha'] in expressions)

    def test_remove_duplicated(self):
        doc = Document("outro teste")
        doc.text = "Olho, Olho."
        expressions = doc.remove_stopwords()

        self.assertTrue(len(expressions),1)

    def test_remove_accents_before_tokezine(self):
        doc = Document("outro teste")
        doc.text = "Cabeça."
        expressions = doc.remove_stopwords()

        self.assertTrue(['Cabeca'] in expressions)
        self.assertTrue(len(expressions),1)

    def test_persist(self):

        text = "o corpo do texto teste";

        doc = Document("apenas um outro teste")
        doc.text = text
        self.assertTrue(doc.save())

        uid = doc._id
        rd = load_document(uid)
        self.assertEqual(rd.text,text)

    def test_recorver_documents(self):
        
        doc = Document("apenas um outro teste")
        self.assertTrue(doc.save())

        doc = Document("apenas um outro teste")
        self.assertTrue(doc.save())

        documents = all_documents()
        self.assertTrue(len(documents) > 0)

    def test_update_document(self):
        text = "o corpo do texto teste";

        doc = Document("apenas um outro teste")
        doc.text = text
        self.assertTrue(doc.save())

        uid = doc._id
        rd = load_document(uid)
        rd.text = "carregando novamente"
        rd.save()

        rd = load_document(uid)
        self.assertEqual(rd.text,"carregando novamente")

unittest.main()

