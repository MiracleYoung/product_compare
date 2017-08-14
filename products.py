#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/13 下午3:07
# @Author  : MiracleYoung
# @File    : products.py



import datetime
import json
from bs4 import BeautifulSoup
import urllib.parse

linux_ua = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
mac_ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

base_headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-HK;q=0.4',
    'Connection': 'keep-alive',
    'Content-Length': '210',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': linux_ua
}


def get_feiniu_product(kw, session, limit=5):
    '''
    飞牛网
    :param kw:
    :param session:
    :param limit:
    :return:
    '''
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
    headers = base_headers.copy()
    headers['Host'] = 'search.feiniu.com'
    headers['Origin'] = 'http://search.feiniu.com'
    headers[
        'Referer'] = 'http://search.feiniu.com/?q=%E7%B4%AB%E8%96%AF%E5%8D%B7&tp=www.0.1000-searchform.1.1502544439776LjQ4'
    res = session.post(url=url, data=data, headers=headers)
    if res.content.strip():
        return res.json()
    return {'list': []}


def parse_jd_product_page(kw, session, limit=5):
    '''
    解析页面，获取jd 商品id
    :param kw:
    :param session:
    :return: {商户id: [商品id, 详情页链接, 商品链接, 价格]}
    '''
    url = 'https://search.jd.com/Search?keyword={0}&enc=utf-8&pvid=529244476a624a88bd98eb325b11028b&wq={0}'.format(kw)
    headers = base_headers.copy()
    kw = urllib.parse.quote(kw)
    headers[
        'Referer'] = 'https://search.jd.com/Search?keyword={0}&enc=utf-8&wq={0}&pvid=d4c7276061c84f1e81e5ea65c7086149'.format(
        kw)
    headers['Host'] = 'search.jd.com'
    res = session.get(url=url).content
    page = BeautifulSoup(res, 'html.parser')
    try:
        product_list = page.find(id='J_goodsList').ul.children
        products = {}
        skip = 0
        for i, product in enumerate(product_list):
            if not product == '\n' and product.select("[data-sku]"):
                product_id = product.select("[data-sku]")[0]['data-sku']
                shop_id = product.select("[data-shopid]")[0]['data-shopid']
                detail_url = product.select(".p-img a['href']")[0]['href'] if \
                    len(product.select(".p-img a['href']")) > 0 else ''
                img_url = product.select(".p-img img['src']")[0]['src'] if \
                    len(product.select(".p-img img['src']")) > 0 else ''
                price = product.select("strong['data-price']")[0]['data-price'] if \
                    len(product.select("strong['data-price']")) > 0 else ''
                products[shop_id] = [product_id, detail_url, img_url, price]
                skip += 1
                if skip + 1 > limit:
                    break
                # print(i)
        return products
    except AttributeError as e:
        return {}


def get_jd_product(shop_ids, session):
    url = 'https://search.jd.com/shop_new.php?ids='
    url = url + ','.join(shop_ids)
    headers = base_headers.copy()
    headers['Host'] = 'search.jd.com'
    headers[
        'Referer'] = 'https://search.jd.com/Search?keyword=%E7%AF%AE%E7%90%83&enc=utf-8&wq=%E7%AF%AE%E7%90%83&pvid=4cf905fb9d30465e9643ab929bf7993c'
    headers.pop('Content-Type')
    headers.pop('Content-Length')
    res = session.get(url=url, headers=headers)
    if res.content.strip():
        return res.json()
    return []



