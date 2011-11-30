# coding: utf-8

import sys
import cyclone.web
import pdb

from os.path import join, abspath, dirname
apipath = abspath(join(dirname(__file__), ".."))
sys.path.append(apipath)

from pythonicus.nlp.base import *


class IndexHandler(cyclone.web.RequestHandler):
    def get(self):
        self.write("hello world")

class DocumentHandler(cyclone.web.RequestHandler):
    def get(self,uid):
        self.set_header("Content-Type", "application/json")

        try:
            doc = load_document(uid)
            self.write(doc.to_json())

        except:
            self.write({})
class AllDocumentsHandler(cyclone.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "application/json")

        documents = all_documents()

        for doc in documents:
            doc = doc.to_json

        self.write(documents)

        try:
            pass
        except:
            self.write([])

class Application(cyclone.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/documents", AllDocumentsHandler),
            (r"/documents/(\w+)", DocumentHandler),
        ]

        settings = {
        #    "static_path": "./static",
        #    "template_path": "./template",
        }

        cyclone.web.Application.__init__(self, handlers, **settings)


