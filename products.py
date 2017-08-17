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
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-HK;q=0.4',
    'User-Agent': linux_ua
}


def get_product(url, headers=None, dom_id=None, dom_class=None):
    '''
    处理所有商品的页面请求，传入函数为返回一个特殊商品的字典解析
    '''

    def _get_product(fn):
        @functools.wraps(fn)
        def __get_product(kw, session, limit=5):
            res = session.get(url=url.format(kw), headers=headers).content
            page = BeautifulSoup(res, 'html.parser')
            try:
                product_ul = page.find(id=dom_id).children if dom_id else page.find(class_=dom_class).children
                skip = 1
                products = []
                for i, product in enumerate(product_ul):
                    if skip > limit:
                        break
                    if not product == '\n':
                        ret = fn(product, kw, session, limit=5)
                        products.append(ret)
                        skip += 1
                        # print(i)
                return products
            except Exception as e:
                print(e)
                return []

        return __get_product

    return _get_product


def feiniu_product(kw, session, limit=5):
    '''
    飞牛网
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
    products = []
    if res.content.strip():
        for product in res.json()['list'][:limit]:
            name = product.get('name', '')
            shop_name = '飞牛网'
            price = product.get('CS000016_price', '') / 100
            detail_url = product.get('item_url', '')
            img_url = product.get('pic', '')
            ret = {
                'name': name.strip('\n'),
                'shop_name': shop_name,
                'price': price,
                'detail_url': detail_url,
                'img_url': img_url
            }
            products.append(ret)
        return products
    return {}


jd_url = 'https://search.jd.com/Search?keyword={0}&enc=utf-8&pvid=529244476a624a88bd98eb325b11028b&wq={0}'
jd_headers = base_headers.copy()
jd_headers['Referer'] = 'https://chaoshi.jd.com/'
jd_headers['Host'] = 'search.jd.com'


@get_product(jd_url, jd_headers, dom_class='gl-warp')
def jd_product(product, kw, session, limit=5):
    '''
    京东
    '''
    name = '\n'.join([p.text for p in product.select('.p-name em')]) if len(product.select('.p-name em')) > 0 else ''
    shop_name = '京东'
    if len(product.select('.p-price strong')) > 0:
        if 'data-price' in product.select('.p-price strong')[0].attrs:
            price = product.select('.p-price strong')[0]['data-price']
        else:
            price = '无'
    else:
        price = '无'
    detail_url = product.select('.p-img a')[0]['href'] if len(product.select('.p-img a')) > 0 else ''
    if len(product.select('.p-img img')) > 0:
        if 'src' in product.select('.p-img img')[0].attrs:
            img_url = product.select('.p-img img')[0]['src']
        else:
            img_url = product.select('.p-img img')[0]['data-lazy-img']
    else:
        img_url = ''
    ret = {
        'name': name.strip('\n'),
        'shop_name': shop_name,
        'price': price,
        'detail_url': detail_url,
        'img_url': img_url
    }
    return ret


tmall_url = 'https://list.tmall.com/search_product.htm?user_id=725677994&type=p&cat=50514008&spm=a3204.7933263.a2227oh.d100&from=chaoshi..pc_1_searchbutton&q={}'
tmall_headers = base_headers.copy()
tmall_headers[
    'referer'] = 'https://list.tmall.com/search_product.htm?q=%B0%FC%D7%D3&user_id=725677994&type=p&cat=50514008&spm=a3204.7084713.a2227oh.d100&from=chaoshi.index.pc_1_searchbutton&smToken=f7c54f27a27847ba97256322636eb293&smSign=OaywForxpkqjLDfCU3rgtA%3D%3D'


@get_product(tmall_url, tmall_headers, dom_id='J_ProductList')
def tmall_product(product, kw, session, limit=5):
    '''
    天猫超市
    '''
    name = product.select('.product-title a')[0].text if len(product.select('.product-title a')) > 0 else ''
    shop_name = '天猫超市'
    price = product.select('.ui-price strong')[0].text if len(product.select('.ui-price strong')) > 0 else ''
    detail_url = product.select('.product-img a')[0]['href'] if len(product.select('.product-img a')) > 0 else ''
    img_url = product.select('.product-img img')[0]['src'] if len(product.select('.product-img img')) > 0 else ''
    ret = {
        'name': name.strip('\n'),
        'shop_name': shop_name,
        'price': price,
        'detail_url': detail_url,
        'img_url': img_url
    }
    return ret


auchan_url = 'http://cy.auchandrive.cn/product/search/?q={}'
auchan_headers = base_headers.copy()
auchan_headers['Host'] = 'cy.auchandrive.cn'
auchan_headers['Referer'] = 'http://cy.auchandrive.cn/'


@get_product(auchan_url, auchan_headers, dom_id='auchan_product_list')
def auchan_product(product, kw, session, limit=5):
    '''
    欧尚
    '''
    name = product.select('#detail_link strong')[1].string.replace('\n', '').replace('\t', '') if product.select(
        '#detail_link strong') else ''
    shop_name = '欧尚'
    price = product.select('b')[1].text if product.select('b') else ''
    detail_url = 'http://cy.auchandrive.cn/{0}'.format(product.select('a')[0]['href']) if product.select(
        'a') else ''
    img_url = product.select('#primary_img')[0]['data-original'] if product.select('#primary_img') else ''
    ret = {
        'name': name,
        'shop_name': shop_name,
        'price': price,
        'detail_url': detail_url,
        'img_url': img_url
    }
    return ret


yhd_url = 'http://search.yhd.com/c-/k{0}/?tp=51.{0}.12.0.3.LrfIR0L-10-2xLwP'
yhd_headers = base_headers.copy()
yhd_headers['Host'] = 'search.yhd.com'
yhd_headers['Referer'] = 'http://search.yhd.com/c-/k%25E8%2582%2589%25E5%258C%2585/?tp=1.1.12.0.3.LrfIAy1-00-8ZNOA'


@get_product(yhd_url, yhd_headers, dom_id='itemSearchList')
def yhd_product(product, kw, session, limit=5):
    '''
    1号店
    '''
    name = product.select('.proName a')[0].text.replace('\n', '').replace('\t', '') if len(
        product.select('.proName a')) > 0 else ''
    shop_name = '1号店'
    price = product.select('.proPrice em')[0].text if len(product.select('.proPrice em')) > 0 else ''
    detail_url = product.select('.proImg a')[0]['href'] if len(product.select('.proImg a')) > 0 else ''
    if  len(product.select('.proImg img')) > 0:
        if 'original' in product.select('.proImg img')[0].attrs:
            img_url = product.select('.proImg img')[0]['original']
        else:
            img_url = product.select('.proImg img')[0]['src']
    else:
        img_url = ''
    ret = {
        'name': name,
        'shop_name': shop_name,
        'price': price,
        'detail_url': detail_url,
        'img_url': img_url
    }
    return ret
