from flask import Flask, render_template, redirect, request, url_for
from flask_login import *
from datetime import *
from colorama import init, Fore, Style # For custom console output formatting
import os, random, math

root = os.path.abspath(os.getcwd())

init(autoreset=True)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'super-secret-key-change-this' # Change this Jasper, for the love of God

# Handle db setup
from src.models import User, Item, db 

db.init_app(app)

with app.app_context():
    db.create_all()

# Seeding
from src.seeding import Seeder

seed = Seeder()

def seedChems(count=150):
    with app.app_context():
        for i in range(count):
            db.session.add(seed.getChem())
    
        db.session.commit()
    print(Style.BRIGHT + Fore.BLUE + f" * Seeded {count} chemicals")
        

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

    # Pagination handler
    page = request.args.get('page', 1, type=int)
    per_page = 10
    itemsPaginated = Item.query.paginate(page=page, per_page=per_page)

    results = []

    # Convert paginated entries into dictionaries
    for item in itemsPaginated:
        results.append({
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "created_at": item.created_at,
            "user_id": item.user_id
        })


    return render_template('browse.html', DISPLAY_INVENTORY=results, PAGE = page, TOTAL_PAGES = math.ceil(Item.query.count() / per_page), PAGE_NUM=page)

# Redirect to index when accessing part of site without proper unauthorization
@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        if not db.session.query(User.id).first(): # Only seed if unseeded
            seedChems()
    
    app.run(host="0.0.0.0", port=5000, debug=True)