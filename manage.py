# -*- encoding: utf-8 -*-

"""API Management and Server Running Module"""

import os
from flask_restful import Api

from app.main import (
        db, # SQLAlchemy Connector dB Object
        create_app
    )

# setting the environment
from dotenv import load_dotenv # Python 3.6+
load_dotenv(verbose = True) # configure .env File or set Environment Variables

app = create_app(os.getenv("PROJECT_ENV_NAME") or "dev") # check config.py
api = Api(app)

### --- List of all Resources --- ###
from app.main.controller import * # import all controllers

# a demo link is provided, delete/uncomment the controller
# this controller is set from app/main/controller/hello_world.py
# also remove app/main/controller/__init__.py
api.add_resource(HelloWorld, "/") # hello-world endpoint

if __name__ == "__main__":
    app.run(
        port = os.getenv("port", 5000), # run the application on default 5000 Port
        host = os.getenv("host", "localhost") # define host, as required
    )
