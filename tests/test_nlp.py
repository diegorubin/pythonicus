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
        tokens = doc.tokenize()
        self.assertEqual(len(tokens),3)

unittest.main()

