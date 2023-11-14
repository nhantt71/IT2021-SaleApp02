from flask import render_template, request, redirect
from flask_login import login_user

import dao
from app import app, login


@app.route('/')
def index():
    kw = request.args.get('kw')

    cates = dao.load_categories()
    prod = dao.load_products(kw=kw)

    return render_template('index.html', categories=cates, products=prod)


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


@app.route('/products/<id>')
def details(id):
    return render_template('details.html')


@app.route('/admin/login', methods=['post'])
def login_admin_process():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

    user = dao.auth_user(username=username, password=password)

    if user:
        login_user(user=user)

    return redirect('/admin')


if __name__ == '__main__':
    from app import admin
    app.run(debug=True)



