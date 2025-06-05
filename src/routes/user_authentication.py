from flask import *
from flask_sqlalchemy import *
from flask_login import *
from flask_wtf import *

from __main__ import app, db, root
from src.models import User

from src.config import ORGANIZATION_NAME

# MAYBE: Implement brute force security
@app.route('/', methods=["GET", "POST"])
def login():
    # Check for POST request and do login
    if request.method == "POST":
        
        # Handle the first login, create new account and label it as an adminestrator
        if not db.session.query(User.id).filter_by(role='admin').first():
            user = User(username=request.form.get("username"), password=request.form.get("password"), role="admin") # Create admin user
            db.session.add(user)
            db.session.commit()
            
            # Continue with login as usual
            user = User.query.filter_by(username=request.form.get("username")).first()
            login_user(user)

            return redirect(url_for("browse"))
        
        else:
            usernameExists = User.query.filter_by(username=request.form.get("username")).first()
            if usernameExists == None:
                flash("Invalid username/password", 'error')
                return redirect(url_for('login'))


            user = User.query.filter_by(username=request.form.get("username")).first()
            # Check for / validate password
            if user.password == request.form.get("password"):
                login_user(user)
                return redirect(url_for("browse"))
            else:
                flash("Invalid username/password", 'error')
                return redirect(url_for('login'))

    return render_template('/login.html', TITLE = ORGANIZATION_NAME)