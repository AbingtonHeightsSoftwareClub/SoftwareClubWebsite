from flask import Flask

app = Flask(__name__)

from app import home_views
from app import error_views
