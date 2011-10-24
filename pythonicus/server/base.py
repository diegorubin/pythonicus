# coding: utf-8

import sys
import cyclone.web
from twisted.python import log
from twisted.internet import reactor

class IndexHandler(cyclone.web.RequestHandler):
    def get(self):
        self.write("hello world")

class Application(cyclone.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
        ]

        #settings = {
        #    "static_path": "./static",
        #    "template_path": "./template",
        #}

        cyclone.web.Application.__init__(self, handlers, **settings)

