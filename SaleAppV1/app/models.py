from sqlalchemy.orm import relationship
from app import db
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Enum
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import enum


class UserRoleEnums(enum.Enum):
    USER = 1
    ADMIN = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100),
                    default="https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg")
    user_role = Column(Enum(UserRoleEnums), default=UserRoleEnums.USER)

    def __str__(self):
        return self.name


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    from app import app

    with app.app_context():
        # db.create_all()
        # import hashlib
        # u1 = User(name='Admin',
        #           username='admin',
        #           password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #           user_role=UserRoleEnums.ADMIN)
        #
        # db.session.add(u1)
        # c1 = Category(name='Tablet')
        # c2 = Category(name='Mobile')
        # c3 = Category(name='Laptop')
        # p1 = Product(name='iPhone 15 Pro Max', price=25000000, category_id=2,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg")
        # p2 = Product(name='Xiaomi Redmi Note 10', price=5000000, category_id=2,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg")
        # p3 = Product(name='Galaxy Note 10 Plus', price=7000000, category_id=2,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg")
        # p4 = Product(name='iPad Pro 2020', price=37000000, category_id=1,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg")
        # p5 = Product(name='Acer Nitro 5', price=21000000, category_id=3,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg")
        # p5 = Product(name='Acer Nitro 5', price=21000000, category_id=3,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg")
        # p5 = Product(name='Acer Nitro 5', price=21000000, category_id=3,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg")
        p6 = Product(name='Acer Nitro 5', price=21000000, category_id=3,
                     image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg")
        p7 = Product(name='Acer Nitro 5', price=21000000, category_id=3,
                     image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg")
        p8 = Product(name='Acer Nitro 5', price=21000000, category_id=3,
                     image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg")
        p9 = Product(name='Acer Nitro 5', price=21000000, category_id=3,
                     image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg")
        p10 = Product(name='Acer Nitro 5', price=21000000, category_id=3,
                     image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg")
        # db.session.add_all([c1, c2, c3])
        # db.session.add_all([p1, p2, p3, p4, p5])
        db.session.add_all([p6, p7, p8, p9, p10])
        db.session.commit()
