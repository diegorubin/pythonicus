# coding: utf-8

import sys
import cyclone.web
import ast

from os.path import join, abspath, dirname
apipath = abspath(join(dirname(__file__), ".."))
sys.path.append(apipath)

from pythonicus.nlp.base import *


class DemoHandler(cyclone.web.RequestHandler):
    def get(self):
        
        static_path = abspath(join(dirname(__file__), "..", "..", "demo"))

        # O esquema do static nao esta rolando
        f = open(static_path + "/index.html")

        self.write(f.read())

class DocumentHandler(cyclone.web.RequestHandler):
    def get(self, uid):
        self.set_header("Content-Type", "application/json")

        try:
            doc = load_document(uid)
            self.write(doc.to_json())
        except:
            self.write({'status' : '500'})

    def put(self, uid):
        self.set_header("Content-Type", "application/json")

        doc = load_document(uid)
        document = ast.literal_eval(self.request.body)

        doc.text = document['text']
        doc.title = document['title']

        doc.save()

        self.write({'status' : '200',
                    'id' : str(doc._id)})

        try:
            pass
        except:
            self.write({'status' : '500'})


class AllDocumentsHandler(cyclone.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "application/json")

        try:
            documents = all_documents()
            arr_documents = []
    
            for doc in documents:
                arr_documents.append(doc.to_json())
    
            self.write({'status' : '200',
                        'documents' : str(arr_documents)})

        except:
            self.write({'status':'500',
                        'documents':[]})

    def post(self):
        self.set_header("Content-Type", "application/json")

        try:
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
            (r"/demo", DemoHandler),
            (r"/documents", AllDocumentsHandler),
            (r"/documents/(\w+)", DocumentHandler),
        ]

        static_path = os.path.join(os.path.dirname(__file__), "static")
        settings = dict(
            static_path = os.path.join(os.path.dirname(__file__), "static")
        )

        print static_path
        print settings

        cyclone.web.Application.__init__(self, handlers, **settings)


