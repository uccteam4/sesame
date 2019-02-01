from flask import Flask, Blueprint

auth = Blueprint("auth", __name__)

import routes
import models