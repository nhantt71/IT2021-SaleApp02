from sqlalchemy.orm import relationship
from app import db
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from flask_sqlalchemy import SQLAlchemy


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    from app import app

    with app.app_context():
        # p1 = Product(name='iPhone 15 Pro Max', category_id=2)
        # p2 = Product(name='Xiaomi Redmi Note 10', category_id=2)
        # p3 = Product(name='Galaxy Note 10 Plus', category_id=1)
        p = Product.query.get(2)
        p.price = 200.69
        # db.session.add(p1)
        # db.session.add(p2)
        # db.session.add(p3)
        db.session.add(p)
        db.session.commit()
        #db.create_all()
