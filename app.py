#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/12 下午9:38
# @Author  : MiracleYoung
# @File    : app.py

from flask import Flask, render_template, jsonify
from products import get_feiniu_product,get_jd_product,get_jd_product_price, parse_jd_product_page
import requests

app = Flask(__name__)

session = requests.session()

@app.route('/', methods=['GET'])
def product():
    return render_template('product.html')

@app.route('/product/<product_name>', methods=['GET'])
def get_products(product_name):
    result = {}
    result_feiniu = get_feiniu_product(product_name, session).json()
    result_jd = get_jd_product(product_name, session).json()
    jd_shop_product = parse_jd_product_page(product_name, session)
    result['feiniu'] = result_feiniu
    result['jd'] = result_jd
    result['jd_shop_product'] = jd_shop_product
    return jsonify(result)

@app.route('/product/jd/price/<id>', methods=['GET'])
def get_jd_product_price(id):
    result = get_jd_product_price(id, session).json()
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
