from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from App import db, app

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
    price = Column(String(10), default=0)
    image = Column(String(300))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        # c1 = Category(name='Di động')
        # c2 = Category(name='Laptop')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
        # db.create_all()

        # p1 = Product(name = 'Samsung Galaxy Fold5', price = '51.990.000', category_id = 1,
        #              image = 'https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/a/m/amsung-galaxy-z-fold-5-1tb.png')
        #
        # p2 = Product(name='iPhone 15 Pro Max', price='46.990.000', category_id=1,
        #              image='https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-pro-256gb_1.png')
        #
        # p3 = Product(name='OPPO Find N3 5G', price='44.990.000', category_id=1,
        #              image='https://cdn.tgdd.vn/Products/Images/42/302953/oppo-find-n3-vang-dong-thumb-600x600.jpg')
        #
        # p4 = Product(name='iPhone 15 Plus', price='34.990.000', category_id=1,
        #              image='https://cdn.tgdd.vn/Products/Images/42/281570/iphone-15-hong-thumb-1-600x600.jpg')
        #
        # p5 = Product(name='OPPO Find X5 Pro 5G', price='32.990.000', category_id=1,
        #              image='https://cdn.tgdd.vn/Products/Images/42/250622/oppo-find-x5-pro-trang-thumb-1-600x600.jpg')
        #
        # p6 = Product(name='ASUS ROG Phone 7 Ultimate', price='29.990.000', category_id=1,
        #              image='https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/1/_/1_365-doc-quyuen.jpg')
        #
        # p7 = Product(name='MacBook Pro M2 Max 2023', price='92.990.000', category_id=2,
        #              image='https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/1/6/16_m2_max.png')
        #
        # p8 = Product(name='Laptop Asus ROG Strix G18', price='70.990.000', category_id=2,
        #              image='https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/t/e/text_ng_n_15__3_18.png')
        #
        # p9 = Product(name='Laptop MSI Creator Z16', price='61.990.000', category_id=2,
        #              image='https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/_/0/_0003_msi-creator-z16-a11uet-217vn-i7.jpg')
        #
        # db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9])
        db.session.commit()
        # db.create_all()
