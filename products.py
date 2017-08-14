#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/13 下午3:07
# @Author  : MiracleYoung
# @File    : products.py



import datetime
import json
from bs4 import BeautifulSoup

base_headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-HK;q=0.4',
    'Connection': 'keep-alive',
    'Content-Length': '210',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
}


def get_feiniu_product(kw, session, limit=5):
    ts = int(datetime.datetime.now().timestamp() * 1000)
    url = 'http://search.feiniu.com/mallHot/getMallHotItems?t={}'.format(ts)
    data = {
        'data': json.dumps({
            'cDistArea': 'CS000016_310100_310106',
            'cp_seq': '',
            'province': 'CS000016',
            'q': kw,
            'resnum': limit,
            'userid': ''
        })
    }
    headers = base_headers
    headers['Host'] = 'search.feiniu.com'
    headers['Origin'] = 'http://search.feiniu.com'
    headers[
        'Referer'] = 'http://search.feiniu.com/?q=%E7%B4%AB%E8%96%AF%E5%8D%B7&tp=www.0.1000-searchform.1.1502544439776LjQ4'
    res = session.post(url=url, data=data, headers=headers)
    return res


def get_jd_product(kw, session, limit=5):
    url = 'https://search.jd.com/shop_new.php?ids=1000073785%2C699829%2C607037%2C85703%2C592539'
    headers = base_headers
    headers['Host'] = 'search.jd.com'
    headers[
        'Referer'] = 'https://search.jd.com/Search?keyword={0}&enc=utf-8&wq={0}&pvid=169f10210cad413bb67492bdc205affe'.format(
        kw)
    res = session.get(url=url, headers=headers)
    return res


def get_jd_product_price(id, session):
    url = 'https://p.3.cn/prices/mgets?skuIds=J_{}'.format(id)
    # url = 'https://p.3.cn/prices/mgets?skuIds=J_4175686'
    headers = base_headers
    headers[
        'Referer'] = 'https://search.jd.com/Search?keyword=%E5%86%85%E8%A3%A4&enc=utf-8&wq=%E5%86%85%E8%A3%A4&pvid=db86a3ebfb6a4b01bef4006a85ecb313'
    headers['Host'] = 'p.3.cn'
    res = session.get(url=url)
    return res


def parse_jd_product_page(kw, session):
    '''
    解析页面，获取jd 商品id
    :param kw:
    :param session:
    :return: {商户id: [商品id, 详情页链接]}
    '''
    url = 'https://search.jd.com/Search?keyword={}&enc=utf-8&pvid=529244476a624a88bd98eb325b11028b'.format(kw)
    headers = base_headers
    headers['Referer'] = 'https://search.jd.com/Search?keyword=%E5%86%85%E8%A3%A4&enc=utf-8&wq=%E5%86%85%E8%A3%A4&pvid=d4c7276061c84f1e81e5ea65c7086149'
    headers['Host'] = 'search.jd.com'
    res = session.get(url=url).content
    page = BeautifulSoup(res)
    product_list = page.find(id='J_goodsList').ul.children
    products = {}
    for i, product in enumerate(product_list):
        if not product == '\n' and product.select("[data-sku]"):
            product_id = product.select("[data-sku]")[0]['data-sku']
            shop_id = product.select("[data-shopid]")[0]['data-shopid']
            img_url = product.select(".p-img a['href']")[0]['href']
            products[shop_id] = [product_id, img_url]
        print(i)
    return products


