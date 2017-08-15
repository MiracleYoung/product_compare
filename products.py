#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/13 下午3:07
# @Author  : MiracleYoung
# @File    : products.py



import datetime
import json
from bs4 import BeautifulSoup
import urllib.parse
import functools
import inspect

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


def get_product(dom_id):
    def _get_product(fn):
        @functools.wraps(fn)
        def wrap(url, session, headers=None, limit=5):
            res = session.get(url=url).content
            page = BeautifulSoup(res, 'html.parser')

            try:
                product_ul = page.find(id=dom_id).children
                products = []
                skip = 1

                ret = fn(product_ul)

                for i, product in enumerate(product_ul):
                    if not product == '\n':
                        name = product.select('.product-title a')[0].text
                        shop_name = '天猫超市'
                        price = product.select('.ui-price strong')[0].text
                        detail_url = product.select('.product-img a')[0]['href']
                        img_url = product.select('.product-img img')[0]['src']
                        products.append({
                            'name': name,
                            'shop_name': shop_name,
                            'price': price,
                            'detail_url': detail_url,
                            'img_url': img_url
                        })
                        skip += 1
                        if skip > limit:
                            break
                return products

            except Exception as e:
                print(e)
                return []

            return ret

        return wrap

    return _get_product



    #
    # url = 'https://list.tmall.com/search_product.htm?&user_id=725677994&type=p&cat=50514008&spm=a3204.7933263.a2227oh.d100&from=chaoshi..pc_1_searchbutton&q={0}'.format(
    #     kw)


def tmall_product(url, session, headers, limit):
    res = session.get(url=url, headers=headers).content
    page = BeautifulSoup(res, 'html.parser')
    try:
        product_ul = page.find(id='J_ProductList').children
        products = []
        skip = 1
        for i, product in enumerate(product_ul):
            if not product == '\n':
                name = product.select('.product-title a')[0].text
                shop_name = '天猫超市'
                price = product.select('.ui-price strong')[0].text
                detail_url = product.select('.product-img a')[0]['href']
                img_url = product.select('.product-img img')[0]['src']
                products.append({
                    'name': name,
                    'shop_name': shop_name,
                    'price': price,
                    'detail_url': detail_url,
                    'img_url': img_url
                })
                skip += 1
                if skip > limit:
                    break
        return products

    except Exception as e:
        print(e)
        return []


def get_tmall_product(kw, session, limit=5):
    url = 'https://list.tmall.com/search_product.htm?user_id=725677994&type=p&cat=50514008&spm=a3204.7933263.a2227oh.d100&from=chaoshi..pc_1_searchbutton&q={0}'.format(
        kw)
    headers = {
        ':authority': 'list.tmall.com',
        ':method': 'GET',
        ':path': '//search_product.htm?user_id=725677994&type=p&cat=50514008&spm=a3204.7933263.a2227oh.d100&from=chaoshi..pc_1_searchbutton&q={}'.format(
            urllib.parse.quote(kw)),
        ':scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-HK;q=0.4',
        'referer': 'https://list.tmall.com/search_product.htm?q=%B0%FC%D7%D3&user_id=725677994&type=p&cat=50514008&spm=a3204.7084713.a2227oh.d100&from=chaoshi.index.pc_1_searchbutton&smToken=f7c54f27a27847ba97256322636eb293&smSign=OaywForxpkqjLDfCU3rgtA%3D%3D',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    res = session.get(url=url, headers=headers).content
    page = BeautifulSoup(res, 'html.parser')
    try:
        product_ul = page.find(id='J_ProductList').children
        products = []
        skip = 1
        for i, product in enumerate(product_ul):
            if not product == '\n':
                name = product.select('.product-title a')[0].text
                shop_name = '天猫超市'
                price = product.select('.ui-price strong')[0].text
                detail_url = product.select('.product-img a')[0]['href']
                img_url = product.select('.product-img img')[0]['src']
                products.append({
                    'name': name,
                    'shop_name': shop_name,
                    'price': price,
                    'detail_url': detail_url,
                    'img_url': img_url
                })
                skip += 1
                if skip > limit:
                    break
        return products

    except Exception as e:
        print(e)
        return []


def get_auchan_product(kw, session, limit=5):
    url = 'http://cy.auchandrive.cn/product/search/?q={0}'.format(kw)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-HK;q=0.4',
        'Connection': 'keep-alive',
        'Host': 'cy.auchandrive.cn',
        'Referer': 'http://cy.auchandrive.cn/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }

    res = session.get(url=url, headers=headers).content
    page = BeautifulSoup(res, 'html.parser')
    try:
        product_ul = page.find(id='auchan_product_list').children
        products = []
        skip = 1
        for i, product in enumerate(product_ul):
            if not product == '\n':
                name = product.select('#detail_link strong')[1].string if product.select('#detail_link strong') else ''
                shop_name = '欧尚'
                price = product.select('b')[1].text if product.select('b') else ''
                detail_url = 'http://cy.auchandrive.cn/{0}'.format(product.select('a')[0]['href']) if product.select(
                    'a') else ''
                img_url = product.select('#primary_img')[0]['src'] if product.select('#primary_img') else ''
                products.append({
                    'name': name,
                    'shop_name': shop_name,
                    'price': price,
                    'detail_url': detail_url,
                    'img_url': img_url
                })
                skip += 1
                if skip > limit:
                    break
        return products

    except Exception as e:
        print(e)
        return []
