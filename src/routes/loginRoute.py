from flask import Blueprint, render_template, request, redirect, url_for


main = Blueprint('loginRoute', __name__)

@main.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login/login.html')

