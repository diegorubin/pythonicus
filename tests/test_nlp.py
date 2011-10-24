import unittest

from pythonicus.nlp.base import *

class test_base(unittest.TestCase):

    def test_tokenize_string(self):
        pt = PersistedText("apenas um teste")
        tokens = pt.tokenize()
        self.assertEqual(len(tokens),3)

unittest.main()

