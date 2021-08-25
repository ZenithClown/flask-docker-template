# -*- encoding: utf-8 -*-

import time

# will be using flask_restful design
from flask_restful import Resource

class HelloWorld(Resource):
    """Hello-World Controller"""

    def get(self):
        # dummy get
        return f"{time.ctime()} | Hello-World"
