from pymongo.connection import Connection
import os

db = None

def get_connection():
    global db

    if db == None:
        print "Conectando ao Mongo"
        connection = Connection('localhost')

        try:
            env = os.environ["PYTHONICUS_ENV"]
        except:
            env = "test"

        if env == "production":
            db = connection['pythonicus_prod']
        else:
            db = connection['pythonicus_test']

    return db


