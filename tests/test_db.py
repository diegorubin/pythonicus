import unittest

try:
    from pythonicus.db.connection import *
except ImportError:
    import sys
    from os.path import join, abspath, dirname
    parentpath = abspath(join(dirname(__file__), '..'))
    sys.path.append(parentpath)
    from pythonicus.db.connection import *


class test_db(unittest.TestCase):

    def test_persist(self):

        db = get_connection()
        
        title = "apenas um title"
        doc = {"title": title}

        db.test.insert(doc)

        db = get_connection()
        doc = db.test.find_one({"title": title})
        self.assertEqual(doc["title"],title) 


unittest.main()

