#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/12 下午9:38
# @Author  : MiracleYoung
# @File    : app.py

from flask import Flask, render_template, jsonify, Response
from products import *
import requests
import json

app = Flask(__name__)

session = requests.session()


@app.route('/', methods=['GET'])
def product():
    return render_template('product.html')


@app.route('/product/feiniu/<product_name>', methods=['GET'])
def feiniu(product_name):
    # 飞牛网
    result = feiniu_product(product_name, session, 100)
    return jsonify(result)

@app.route('/product/jd/<product_name>', methods=['GET'])
def jd(product_name):
    # 京东
    result = jd_product(product_name, session, 100)
    # return Response(json.dumps(result),  mimetype='application/json')
    return jsonify(result)

@app.route('/product/tmall/<product_name>', methods=['GET'])
def tmall(product_name):
    # 天猫超市
    result = tmall_product(product_name, session, 100)
    return jsonify(result)

@app.route('/product/auchan/<product_name>', methods=['GET'])
def auchan(product_name):
    # 欧尚
    result = auchan_product(product_name, session, 100)
    return jsonify(result)

@app.route('/product/yhd/<product_name>', methods=['GET'])
def yhd(product_name):
    # 1号店
    result = yhd_product(product_name, session, 100)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
