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
        doc.set_text("apenas um teste")
        tokens = doc.tokenize()
        self.assertEqual(len(tokens),3)

    def test_persist(self):

        text = "o corpo do texto teste";

        doc = Document("apenas um outro teste")
        doc.set_text(text)
        self.assertEqual(doc.save(),True)

        #rd = load_document(doc.get_uid())
        #self.assertEqual(rd.get_text(),text)


unittest.main()

