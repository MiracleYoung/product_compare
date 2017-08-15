#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/12 下午9:38
# @Author  : MiracleYoung
# @File    : app.py

from flask import Flask, render_template, jsonify
from products import *
import requests

app = Flask(__name__)

session = requests.session()


@app.route('/', methods=['GET'])
def product():
    return render_template('product.html')


@app.route('/product/<product_name>', methods=['GET'])
def get_products(product_name):
    result = {}
    # 飞牛网
    # result_feiniu = get_feiniu_product(product_name, session, 5)
    # result['feiniu'] = result_feiniu
    #
    # # 京东
    # jd_shop_product = parse_jd_product_page(product_name, session, 5)
    # result['jd_shop_product'] = jd_shop_product
    #
    # shop_ids = [shop_id for shop_id, _ in jd_shop_product.items()]
    # result_jd = get_jd_product(shop_ids, session)
    # result['jd'] = result_jd

    # 天猫超市
    result_tmall = get_tmall_product(product_name, session, 5)
    result['tmall'] = result_tmall

    # 欧尚
    result_auchan = get_auchan_product(product_name, session, 5)
    result['auchan'] = result_auchan
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
