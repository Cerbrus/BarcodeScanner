import os

from flask import Flask

app = Flask(__name__)

from supermarktconnector.ah import AHConnector

@app.route('/barcode/<barcode>', methods=['GET'])
def get_product(barcode):
    print('barcode:', barcode)

    connector = AHConnector()
    return connector.get_product_by_barcode(barcode)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
