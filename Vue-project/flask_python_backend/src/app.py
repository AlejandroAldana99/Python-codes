import os, sys

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from flask import Flask
from flask_cors import CORS

from src.helpers.database import Database
from src.controller import orderRoutes
from src.controller import productRoutes

app = Flask(__name__)
app.register_blueprint(orderRoutes)
app.register_blueprint(productRoutes)
CORS(app)

db = Database.connect()

if __name__ == '__main__':
    app.debug = True
    app.run()