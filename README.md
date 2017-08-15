# 小胖比价器

## 前言
为了满足更多家庭女性的日常购物需求，现推出**小胖购物车**，一键比价。

- 目前罗列的网商有：
    - 大润发
    - 京东超市
    - 天猫超市
    - 欧尚
    - 1号店
    

## 使用

pip install -r requirements.txt

- dev

    python wsgi.py
    
- deploy

    gunicorn -c gunicorn.conf wsgi:app

    
---

## Version:

### v1.0
    version 1.0 全部完成。
    通过nginx 转发 gunicorn 完成web service。
    前端通过parallel 实现多线程同时请求数据接口，以更快获得数据。
    除了飞牛网通过接口请求获得数据外，其他统一处理成爬取页面。
