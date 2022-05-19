from ..student import studentbp
from flask import render_template


@studentbp.app_errorhandler(404)
def notFound(e):
  return render_template('err.html'),404