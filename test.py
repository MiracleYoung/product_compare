#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/15 上午6:26
# @Author  : MiracleYoung
# @File    : test.py

import requests

from products import get_taobao_product
import requests



if __name__ == '__main__':
    product = get_taobao_product('肉包', requests.session())
