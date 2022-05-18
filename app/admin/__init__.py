
from flask import Blueprint

adminbp = Blueprint("adminbp",__name__,static_folder="./../static",template_folder="./../templates")


from . import views