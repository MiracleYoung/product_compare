#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/15 上午6:26
# @Author  : MiracleYoung
# @File    : test.py

import requests

from products import parse_jd_product_page

if __name__ == '__main__':
    parse_jd_product_page('短裤', requests.session())