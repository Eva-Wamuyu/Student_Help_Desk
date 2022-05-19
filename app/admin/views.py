from . import adminbp 
from flask import Flask, render_template, url_for
from ..models import  User, Request
from sqlalchemy import text
from .. import db

@adminbp.route('/')
def home():
    student_count = User.query.filter(User.role == 'Student').count()
    mentor_count = User.query.filter(User.role == 'Mentor').count()

    sql = text("select role from user")
    result = db.engine.execute(sql)
    roles = [row[0] for row in result]
    print (roles)
    return render_template('admin/dashboard.html', students = student_count, mentors = mentor_count)