# coding: utf-8

import sys
import cyclone.web

class IndexHandler(cyclone.web.RequestHandler):
    def get(self):
        self.write("hello world")

class DocumentHandler(cyclone.web.RequestHandler):
    def get(self):
        pass


class Application(cyclone.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/documents", DocumentHandler),
        ]

        settings = {
        #    "static_path": "./static",
        #    "template_path": "./template",
        }

        cyclone.web.Application.__init__(self, handlers, **settings)


