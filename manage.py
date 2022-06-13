# -*- encoding: utf-8 -*-

"""API Management and Server Running Module"""

from os import getenv
from app import app

if __name__ == "__main__":
    app.run(
        port = getenv("port", 5000), # run the application on default 5000 Port
        # localhost is required to run the code from m/c
        # else, 0.0.0.0 can be used for docker container
        host = getenv("host", "0.0.0.0") # define host, as required
    )
