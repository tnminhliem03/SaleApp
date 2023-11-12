from flask import render_template, request, redirect
import  dao
from App import app, login
from flask_login import UserMixin, login_user

@app.route('/')
def index():
    kw = request.args.get('kw')

    cates = dao.load_categories()
    products = dao.load_products(kw)

    return render_template('index.html', categories = cates, products = products)

@app.route('/admin/login', methods = ['get', 'post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.check_login(username = username, password = password)

    if user:
        login_user(user = user)

    return redirect('/admin')

@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == '__main__':
    from App import admin
    app.run(debug=True)