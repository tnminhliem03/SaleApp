import math

from flask import render_template, request, redirect, session, jsonify
import  dao
import utils
from App import app, login
from flask_login import login_user, logout_user, login_required

@app.route('/')
def index():
    kw = request.args.get('kw')
    cates_id = request.args.get('cates_id')
    page = request.args.get('page')

    products = dao.load_products(kw, cates_id, page)

    num = dao.count_product()

    return render_template('index.html', products = products,
                           pages = math.ceil(num / app.config['PAGE_SIZE']))

@app.route('/admin/login', methods = ['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.auth_user(username = username, password = password)

    if user:
        login_user(user = user)

    return redirect('/admin')

@app.route('/login', methods = ['get', 'post'])
def process_user_login():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = dao.auth_user(username=username, password=password)

        if user:
            login_user(user=user)
            next = request.args.get('next')

        return redirect('/' if next is None else next)

    return render_template('login.html')

@app.route('/logout')
def process_user_logout():
    logout_user()
    return redirect('/login')

@app.route('/register', methods = ['get', 'post'])
def register_user():
    err_msg = None

    if request.method.__eq__('POST'):
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        if password.__eq__(confirm):
            try:
                dao.add_user(name = request.form.get('name'), username= request.form.get('username')
                             , password = password, avatar= request.files.get('avatar'))
            except Exception as ex:
                print(str(ex))
                err_msg = 'Hệ thống đang bị lỗi!!!!'
            else:
                return redirect('/login')
        else:
            err_msg = 'Mật khẩu không trùng nhau!'

    return render_template('/register.html', err_msg = err_msg)

@app.route('/api/cart', methods = ['post'])
def add_to_cart():
    data = request.json

    cart = session.get('cart')

    if cart is None:
        cart = {}

    id = str(data.get("id"))
    if id in cart: # sp đã có trong giỏ hàng
        cart[id]['quantity'] += 1
    else: # sp chưa có trong giỏ hàng
        cart[id] = {
            "id": id,
            "name": data.get('name'),
            "price": data.get('price'),
            "quantity": 1
        }

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))

@app.route('/api/cart/<product_id>', methods = ['put'])
def update_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        quantity = request.json.get('quantity')
        cart[product_id]['quantity'] = int(quantity)

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))

@app.route('/api/cart/<product_id>', methods = ['delete'])
def delete_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
       del cart[product_id]

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/api/pay', methods = ['post'])
@login_required
def pay():
    try:
        dao.add_receipt(session.get('cart'))
    except:
        return jsonify({'status': 500, 'err_msg': "..."})
    else:
        del session['cart']
        return jsonify({'status': 200})

@app.route('/login')
def user_login():
    return render_template('login.html')

@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

@app.context_processor
def common_response():
    return {
        'categories': dao.load_categories(),
        'cart': utils.count_cart(session.get('cart'))
    }

if __name__ == '__main__':
    from App import admin
    app.run(debug=True)