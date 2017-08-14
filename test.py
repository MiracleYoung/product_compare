#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/15 上午6:26
# @Author  : MiracleYoung
# @File    : test.py

import requests

from products import parse_jd_product_page, base_headers
import requests


def get_jd_product():
    url = 'https://search.jd.com/shop_new.php?ids=102806%2C1000004451%2C1000004786%2C1000010862%2C1000004425%2C185024%2C32000%2C156918%2C597645%2C98721%2C1000005656%2C110051%2C1000004252'
    headers = base_headers
    headers['Host'] = 'search.jd.com'
    headers[
        'Referer'] = 'https://search.jd.com/Search?keyword=%E7%AF%AE%E7%90%83&enc=utf-8&wq=%E7%AF%AE%E7%90%83&pvid=4cf905fb9d30465e9643ab929bf7993c'
    session = requests.session()
    res = session.get(url=url, headers=headers)
    return res

if __name__ == '__main__':
    jd_product = get_jd_product()
