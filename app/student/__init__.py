
from flask import Blueprint

studentbp = Blueprint("studentbp",__name__,static_folder="./../static",template_folder="./../templates")


from . import views
