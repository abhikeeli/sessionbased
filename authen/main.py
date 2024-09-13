from flask import Blueprint
from flask_login import login_required, current_user

main = Blueprint('main', __name__)
@main.route('/')
def index():
    return 'Index'


@main.route('/profile')
@login_required
def profile():
    name=current_user.name
    return "{}".format(name)