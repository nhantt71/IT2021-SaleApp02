from flask import Flask, render_template, request
import dao


app = Flask(__name__)


@app.route('/')
def index():
    kw = request.args.get('kw')

    cates = dao.load_categories()
    prod = dao.load_products(kw=kw)

    return render_template('index.html', categories=cates, products=prod)


@app.route('/products/<id>')
def details(id):
    return render_template('details.html')


if __name__ == '__main__':
    app.run(debug=True)




