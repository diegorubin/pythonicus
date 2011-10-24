import unittest


try:
    from pythonicus.nlp.base import *
except ImportError:
    import sys
    from os.path import join, abspath, dirname
    parentpath = abspath(join(dirname(__file__), '..'))
    #srcpath = join(parentpath, 'src')
    sys.path.append(parentpath)
    from pythonicus.nlp.base import *


class test_base(unittest.TestCase):

    def test_tokenize_string(self):
        pt = PersistedText("apenas um teste")
        tokens = pt.tokenize()
        self.assertEqual(len(tokens),3)

unittest.main()

