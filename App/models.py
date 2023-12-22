from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Float, DateTime, Boolean
from sqlalchemy.orm import relationship
from App import db, app
from flask_login import UserMixin
import enum
from datetime import datetime

class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key= True, autoincrement= True)
    name = Column(String(50), nullable= False, unique= True)
    username = Column(String(50), nullable= False, unique= True)
    password = Column(String(100), nullable= False)
    avatar = Column(String(300), default=
    'https://scontent.fsgn8-4.fna.fbcdn.net/v/t39.30808-1/383224139_1986909575016916_4431354892872745129_n.jpg?stp=dst-jpg_p320x320&_nc_cat=107&ccb=1-7&_nc_sid=5f2048&_nc_ohc=cWuBop4WQAoAX-8BwyA&_nc_ht=scontent.fsgn8-4.fna&oh=00_AfDZTDlpnbwifU1zMrxts1NUUXC2hxrq_lvPKPtbnjoCmw&oe=65536435')
    user_role = Column(Enum(UserRoleEnum), default = UserRoleEnum.USER)
    receipts = relationship('Receipt', backref='user', lazy=True)

    def __str__(self):
        return self.name

class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)
    def __str__(self):
        return self.name

class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(300))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    receipt_details = relationship('ReceiptDetails', backref='product', lazy=True)
    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key= True, autoincrement= True)
    active = Column(Boolean, default= True)
    created_date = Column(DateTime, default= datetime.now())

class Receipt(BaseModel):
    user_id = Column(Integer, ForeignKey(User.id), nullable= True)
    receipt_details = relationship('ReceiptDetails', backref='receipt', lazy=True)

class ReceiptDetails(BaseModel):
    quantity = Column(Integer, default= 0)
    price = Column(Float, default= 0)
    receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable= False)
    product_id = Column(Integer, ForeignKey(Product.id), nullable= False)

if __name__ == '__main__':
    with app.app_context():
        # db.create_all()

        c1 = Category(name='Điện thoại')
        c2 = Category(name='Laptop')
        c3 = Category(name = 'Tablet')
        c4 = Category(name = 'Smartwatch')
        db.session.add_all([c1, c2, c3, c4])
        db.session.commit()

        p1 = Product(name='Samsung Galaxy Fold5', price=51990000, category_id=1,
                     image='https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/a/m/amsung-galaxy-z-fold-5-1tb.png')

        p2 = Product(name='OPPO Find N3 5G', price=44990000, category_id=1,
                     image='https://cdn.tgdd.vn/Products/Images/42/302953/oppo-find-n3-vang-dong-thumb-600x600.jpg')

        p3 = Product(name='iPhone 15 Plus', price=34990000, category_id=1,
                     image='https://cdn.tgdd.vn/Products/Images/42/281570/iphone-15-hong-thumb-1-600x600.jpg')

        p4 = Product(name='OPPO Find X5 Pro 5G', price=32990000, category_id=1,
                      image='https://cdn.tgdd.vn/Products/Images/42/250622/oppo-find-x5-pro-trang-thumb-1-600x600.jpg')

        p5 = Product(name='MacBook Pro M2 Max 2023', price=92990000, category_id=2,
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/1/6/16_m2_max.png')

        p6 = Product(name='Laptop Asus ROG Strix G18', price=70990000, category_id=2,
                     image='https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/t/e/text_ng_n_15__3_18.png')

        p7 = Product(name='Laptop MSI Creator Z16', price=61990000, category_id=2,
                     image='https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/_/0/_0003_msi-creator-z16-a11uet-217vn-i7.jpg')

        p8 = Product(name='Laptop LG Gram 2023', price=50990000, category_id=2,
                     image='https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/t/e/text_d_i_10_.png')

        p9 = Product(name='Garmin Fenix 7X Pro Titanium', price=25990000, category_id=3,
                      image='https://cdn.tgdd.vn/Products/Images/7077/308517/garmin-fenix-7x-pro-solar-titanium-xam-tb-1-600x600.jpg')

        p10 = Product(name='Apple Watch Ultra Titanium', price=23990000, category_id=3,
                      image='https://cdn.tgdd.vn/Products/Images/7077/289814/apple-watch-ultra-alpine-m-cam-thumbnew-1-600x600.jpg')

        p11 = Product(name='Samsung Galaxy Watch5 Pro', price=11990000, category_id=3,
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/s/a/sansung_2__2.png')

        p12 = Product(name='Huawei Watch Buds', price=10990000, category_id=3,
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/h/u/huawei_13_.png')

        p13 = Product(name='iPad Pro 2022 M2', price=38990000, category_id=4,
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/ipad-pro-13-select-wifi-spacegray-202210-02_3_3.jpg')

        p14 = Product(name='Samsung Galaxy Tab S9 Ultra', price=38990000, category_id=4,
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/t/a/tab-s9-ultra-bac-1_1.jpg')

        p15 = Product(name='OPPO Pad 2', price=14990000, category_id=4,
                      image='https://cdn.tgdd.vn/Products/Images/522/303146/oppo-pad-2-thumb-600x600.jpeg')

        p16 = Product(name='Xiaomi Pad 6', price=10490000, category_id=4,
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/x/i/xiaomi-mi-pad-6-8gb-128gb_4__1.jpg')

        db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16])
        db.session.commit()

        import hashlib
        u = User(name = 'Admin', username = 'admin',
                 password = str(hashlib.md5('123456'.encode('utf-8')).hexdigest()), user_role = UserRoleEnum.ADMIN)
        db.session.add(u)
        db.session.commit()