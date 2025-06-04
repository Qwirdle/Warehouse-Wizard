from flask import Flask, render_template, redirect, request, url_for
from flask_login import *
from datetime import *
from colorama import init, Fore, Style # For custom console output formatting
import os, random

root = os.path.abspath(os.getcwd())

init(autoreset=True)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'super-secret-key-change-this' # Change this Jasper, for the love of God

# Handle db setup
from src.models import User, Item, db 

db.init_app(app)

with app.app_context():
    db.create_all()

# Import routes
from src.routes.user_authentication import login

# Will fix when inconvenience is encountered <3
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route('/browse/')
@login_required
def browse():
    user = User.query.filter_by(username=current_user.username).first()

    return render_template('browse.html')

# Redirect to index when accessing part of site without proper unauthorization
@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('login'))

if __name__ == '__main__':
    
    app.run(host="0.0.0.0", port=5000, debug=True)