import os

from flask import Flask, redirect, render_template, request
from lib import ah
from lib.helpers import build_headers

app = Flask(__name__)


@app.route("/")
def home():
    return redirect("/barcode")


@app.route('/barcode', methods=['GET'])
def list_products():
    sort = request.args.get('sort') or 'title'
    order = request.args.get('order')

    sortBy = {
        'barcode': lambda x: x['barcode'],
        'title': lambda x: x['data']['title'],
        'price': lambda x: 'priceBeforeBonus' in x['data'] and x['data']['priceBeforeBonus'] or float('inf')
    }[sort]

    headers = build_headers(
        {'barcode': 'Barcode', 'title': 'Title', 'price': 'Price'},
        sort,
        order
    )

    products = ah.list_products()
    sorted_products = sorted(products, key=sortBy, reverse=order == 'desc')

    return render_template('index.html', products=sorted_products, headers=headers)


@app.route('/barcode/<gtin>', methods=['GET'])
def get_product(gtin):
    print('gtin:', gtin)
    return ah.find_product(gtin)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
