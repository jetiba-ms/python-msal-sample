import sys
import os
import logging
import azure.functions as func

from azf_wsgi import AzureFunctionsWsgi

dir_path = os.path.dirname(os.path.realpath("secureFlaskApp/__init__.py"))
sys.path.insert(0, dir_path)
print(sys.path)
from ..secureFlaskApp import app as application

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return AzureFunctionsWsgi(application).main(req)