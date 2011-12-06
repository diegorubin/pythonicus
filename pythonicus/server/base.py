# coding: utf-8

import sys
import cyclone.web
import ast

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
            self.write({'status' : '500'})

class AllDocumentsHandler(cyclone.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "application/json")

        documents = all_documents()
        arr_documents = []

        for doc in documents:
            arr_documents.append(doc.to_json())

        self.write({'status' : '200',
                    'documents' : str(arr_documents)})

        try:
            pass
        except:
            self.write({'status':'500',
                        'documents':[]})

    def post(self):

        try:
            self.set_header("Content-Type", "application/json")
    
            document = ast.literal_eval(self.request.body)
    
            d = Document()
            d.__dict__ = document
            d.save()
    
            self.write({'status' : '200',
                        'id' : str(d._id)})

        except:
            self.write({'status': '500',
                        'erro' : 'documento não pode ser salvo'})

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


