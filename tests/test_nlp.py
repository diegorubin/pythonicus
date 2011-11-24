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
        self.assertEqual(len(tokens),3)

    def test_persist(self):

        text = "o corpo do texto teste";

        doc = Document("apenas um outro teste")
        doc.text = text
        self.assertEqual(doc.save(),True)

        uid = doc._id
        rd = load_document(uid)
        self.assertEqual(rd.text,text)

    def test_recorver_documents(self):
        
        doc = Document("apenas um outro teste")
        self.assertEqual(doc.save(),True)

        doc = Document("apenas um outro teste")
        self.assertEqual(doc.save(),True)

        documents = all_documents()
        self.assertEqual(len(documents) > 0, True)


unittest.main()

