from flask import Flask, Blueprint
from app import login_manager

auth = Blueprint("auth", __name__)

import routes
import models
import forms