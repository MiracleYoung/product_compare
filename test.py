#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/15 上午6:26
# @Author  : MiracleYoung
# @File    : test.py

import requests

from products import get_tmall_product
import requests

import inspect
import functools

from bs4 import BeautifulSoup

html = '''
<!DOCTYPE HTML>



<html>

<head>
	<meta charset="gbk" />
	<meta name="renderer" content="webkit" />
	<meta http-equiv="X-UA-Compatible" content="IE=Edge" />
	<link rel="dns-prefetch" href="//g.alicdn.com" />
	<link rel="dns-prefetch" href="//img.alicdn.com" />
	<link rel="dns-prefetch" href="//gm.mmstat.com" />
	<link rel="dns-prefetch" href="//ald.taobao.com" />
	<link rel="dns-prefetch" href="//bar.tmall.com" />
	<meta name="spm-id" content="a3204.7933263" />
	<title>包子--天猫超市-天猫Tmall.com-上天猫，就购了-理想生活上天猫</title>
	<link rel="shortcut icon" href="//img.alicdn.com/tfs/TB1XlF3RpXXXXc6XXXXXXXXXXXX-16-16.png" type="image/x-icon" />
	<script>
		window.g_config = window.g_config || {};
		window.g_config.devId = "pc";
		window.g_config.headerVersion = '1.0.0';
		window.g_config.pageId = 'chaoshi';
		window.g_config.bizId = 'chaoshi';
		window.g_config.isMarket = true;
		window.g_config.loadModulesLater = true;
		window.g_config.sl = 'vm';
	</script>

	<style>
		#footer .footer-info {
			width: auto !important
		}

		#footer .tmall-intro {
			width: 990px !important
		}
	</style>
	<script>
		g_config.notInitSearchBar = true;
		g_config.closeMiniBag = true;
		g_config.tmallConfig = g_config.tmallConfig || {};
		g_config.tmallConfig.commonJS = g_config.tmallConfig.commonJS || {};
		g_config.tmallConfig.commonJS.miniBag = { off: true };
	</script>
	<!-- globalmodule version from fragment: 3.0.79 -->
	<link rel="stylesheet" href="//g.alicdn.com/??mui/global/3.0.28/global.css" />
	<script src="//g.alicdn.com/??kissy/k/1.4.14/seed-min.js,mui/seed/1.4.8/seed.js,mui/globalmodule/3.0.79/seed.js,mui/btscfg-g/3.0.0/index.js,mui/bucket/3.0.4/index.js,mui/globalmodule/3.0.79/global-mod-pc.js,mui/globalmodule/3.0.79/global-mod.js,mui/global/3.0.28/global-pc.js,mui/global/3.0.28/global.js,tm/list/2.22.0/mui-seed.js,tm/list/2.22.0/seed.js,mui/kissy-polyfill/4.0.12/index.js"></script>
	<script src="//g.alicdn.com/secdev/pointman/js/index.js" app="tmall"></script>
	<script>
		TB.environment.isApp = true;
		TB.environment.passCookie = true;
	</script>

	<!-- /chaoshi/header_banner_pc /chaoshi/pc_nav /chaoshi/footer_v2 -->
	<link rel="stylesheet" href="//g.alicdn.com/??mui/chaoshi-pc-base/4.0.7/index.css,mui/chaoshi-pc-base/4.0.7/list/list.css"
	/>
	<script src="//g.alicdn.com/??mui/chaoshi-pc-base/4.0.7/seed.js,mui/chaoshi-pc-base/4.0.7/list/list.js"></script>

</head>

<body>
	<script>
		with (document) with (body) with (insertBefore(createElement("script"), firstChild)) setAttribute("exparams", "category=50514008&userid=667497065&at_bucketid=sbucket%5f3&at_mall_pro_re=281&aplus&at_rn=7fc97be1a643f68eb11af46ce63620c1&yunid=&37b47104df5b6&asid=AWkyyScQcpNZ62zFEQAAAACL0KFuISdaRw==", id = "tb-beacon-aplus", src = (location > "https" ? "//g" : "//g") + ".alicdn.com/alilog/mlog/aplus_v2.js")
	</script>

	<div id="mallPage" class="  tmall-chaoshi  page-market">
		<!--from fragment-->
		<div id="site-nav" data-spm="a2226mz">
			<div id="sn-bg">
				<div class="sn-bg-right">
				</div>
			</div>
			<div id="sn-bd">
				<b class="sn-edge"></b>
				<div class="sn-container">
					<p id="login-info" class="sn-login-info"></p>
					<ul class="sn-quick-menu">
						<li class="sn-mytaobao menu-item j_MyTaobao">
							<div class="sn-menu">
								<a class="menu-hd" href="//i.taobao.com/my_taobao.htm" target="_top" rel="nofollow">我的淘宝<b></b></a>
								<div class="menu-bd">
									<div class="menu-bd-panel" id="myTaobaoPanel">
										<a href="//trade.taobao.com/trade/itemlist/list_bought_items.htm?t=20110530" target="_top" rel="nofollow">已买到的宝贝</a>
										<a href="//trade.taobao.com/trade/itemlist/list_sold_items.htm?t=20110530" target="_top" rel="nofollow">已卖出的宝贝</a>
									</div>
								</div>
							</div>
						</li>
						<li class="sn-seller-center hidden j_SellerCenter">
							<a target="_top" href="//mai.taobao.com/seller_admin.htm">商家中心</a>
						</li>
						<li class="sn-mybrand"><i class="mui-global-iconfont">&#x3449;</i>
							<a target="_top" id="J_SnMyBrand" class="sn-mybrand-link" href="//mybrand.tmall.com?scm=1048.1.1.1">我关注的品牌</a>
						</li>
						<li class="sn-cart"><i class="mui-global-iconfont">&#xf0148;</i>
							<a class="sn-cart-link" href="//cart.tmall.com/cart/myCart.htm?from=btop" target="_top" rel="nofollow">购物车
                    </a>
						</li>
						<li class="sn-favorite menu-item">
							<div class="sn-menu">
								<a class="menu-hd" href="//shoucang.taobao.com/shop_collect_list.htm?scjjc=c1" target="_top" rel="nofollow">收藏夹<b></b></a>

								<div class="menu-bd">
									<div class="menu-bd-panel">
										<a href="//shoucang.taobao.com/item_collect.htm" target="_top" rel="nofollow">收藏的宝贝</a>
										<a href="//shoucang.taobao.com/shop_collect_list.htm" target="_top" rel="nofollow">收藏的店铺</a>
									</div>
								</div>
							</div>
						</li>
						<li class="sn-separator"></li>
						<li class="sn-mobile">
							<i class="mui-global-iconfont">&#x3448;</i>
							<a title="天猫无线" target="_top" class="sn-mobile-link" href="//pages.tmall.com/wow/portal/act/app-download?scm=1027.1.1.1">手机版</a>
						</li>
						<li class="sn-home">
							<a href="//www.taobao.com/">淘宝网</a>
						</li>
						<li class="sn-seller menu-item">
							<div class="sn-menu J_DirectPromo">
								<a class="menu-hd" href="//mai.taobao.com" target="_top">商家支持<b></b></a>
								<div class="menu-bd sn-seller-lazy">
								</div>
							</div>
						</li>
						<li class="sn-sitemap">
							<div class="sn-menu">
								<h3 class="menu-hd"><i class="mui-global-iconfont">&#xe601;</i><span>网站导航</span><b></b></h3>
								<div class="menu-bd sn-sitemap-lazy sn-sitemap-bd" data-spm="a2228l4">
								</div>
							</div>
						</li>
					</ul>
				</div>
			</div>
		</div>

		<div id="header" class="mallChn" data-spm="a2226n0">
			<div class="headerLayout">
				<div class="headerCon  hasSubLogo ">
					<h1 id="mallLogo">
						<span class="mlogo">
   
<a href="//chaoshi.tmall.com?notjump=true&_ig=logo" title="天猫超市-chaoshi.tmall.com"><s></s>天猫超市-chaoshi.tmall.com</a>
   </span>
					</h1>

					<div class="header-extra">
						<div class="header-banner">
							<ul class="market-feature">
								<li>
									<a href="///pages.tmall.com/wow/chaoshi/act/yizhanshigouqi?spm=a312d.7832034.0.0.snz6y7">
										<s>&#x347d;</s>一站式购齐</a>
								</li>
								<li>
									<a href="//service.tmall.com/support/tmall/knowledge-1137790.htm">
										<s>&#x3489;</s>满88包邮</a>
								</li>
								<li class="license"><a href="//pages.tmall.com/wow/chaoshi/act/paper-list"><img src="//img.alicdn.com/tps/i1/TB1L25iFFXXXXXcbpXXgBrbGpXX-36-36.png"/></a></li>
							</ul>
						</div>
						<div id="mallSearch" class="mall-search">
							<form name="searchTop" action="//list.tmall.com//search_product.htm" class="mallSearch-form clearfix" target="_top">
								<fieldset>
									<legend>天猫搜索</legend>
									<div class="mallSearch-input clearfix">
										<label for="mq">搜索 天猫 商品/品牌/店铺</label>

										<div class="s-combobox">
											<div class="s-combobox-input-wrap">
												<input type="text" name="q" accesskey="s" autocomplete="off" x-webkit-speech="" x-webkit-grammar="builtin:translate" value="包子"
												 id="mq" autocomplete="off" />
											</div>
										</div>
										<button type="submit"><i>&#x355d;</i>搜索<s></s>
 </button>
										<input id="J_Type" type="hidden" name="type" value="p" />
										<input id="J_MallSearchStyle" type="hidden" name="style" value="">
										<input id="J_Cat" type="hidden" name="cat" value="all" />
										<input type="hidden" name="vmarket" value="">
									</div>
								</fieldset>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div class="tm-chaoshi-nav" data-spm="1998159256">
			<div class="layout">
				<div class="nav-extra">
					<div id="cat">所有产品分类</div>
					<div id="J_NavCart"></div>
					<a class="my-welfare" href="//chaoshi.tmall.com/oclottery/oclottery.htm"><span></span>我的福利</a>
				</div>
			</div>
		</div>
		<style>
			.hot-query {
				display: none;
			}
		</style>

		<div id="content">















			<div class="main">
				<div class="main-wrap">
					<div class="mallCrumbs mb10 clearfix">
						<h2 class="offScreen">网站面包屑</h2>
						<p class="mallCrumbs-count">
							相关商品<em>281</em>件
						</p>
						<ul class="mallCrumbs-nav" id="J_crumbs">
							<li class="mallCrumbs-nav-item">
								<a href="//list.tmall.com/search_product.htm?at_topsearch=1&search_condition=1&cat=50514008&user_id=725677994&q=%B0%FC%D7%D3">
									<!-- onclick="atpanelClick('1', '2', '', '', 'spu-rightnav');" -->
									“包子”
								</a>
								<b class="icon"></b>
							</li>
						</ul>
					</div>


					<!-- 品牌、属性筛选区 start -->
					<div class="navigation mb10 clearfix" id="J_ColPropNavigation" _title="智能类目导航区" _detail="分类不再需要一步步点击，相关的热门分类直接呈现">
						<h2 class="offScreen">相关品牌、属性筛选区</h2>



						<form id="J_multiSelect" action="/search_product.htm" method="get">
							<h3 class="offScreen">请按按下列属性进一步筛选商品</h3>

							<div id="J_RecommendProp" class="colProp">



								<div class="colProp-item clearfix">
									<h4 class="colProp-title">品牌：</h4>
									<ul class="colProp-list">
										<li><a fromtab="spu-brand" brand="274838064" pos="1" title="易果生鲜" href="?cat=50514008&amp;brand=274838064&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100&is=brand"><b class="multi-icon"></b>易果生鲜</a></li>
										<li><a fromtab="spu-brand" brand="3219783" pos="2" title="ANGEL/安琪" href="?cat=50514008&amp;brand=3219783&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100&is=brand"><b class="multi-icon"></b>ANGEL/安琪</a></li>
										<li><a fromtab="spu-brand" brand="60418984" pos="3" title="Baker Dream/百钻" href="?cat=50514008&amp;brand=60418984&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100&is=brand"><b class="multi-icon"></b>Baker Dream/百钻</a></li>
										<li><a fromtab="spu-brand" brand="289032041" pos="4" title="水妈妈（泰国）" href="?cat=50514008&amp;brand=289032041&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100&is=brand"><b class="multi-icon"></b>水妈妈（泰国）</a></li>
										<li><a fromtab="spu-brand" brand="27605564" pos="5" title="风筝牌" href="?cat=50514008&amp;brand=27605564&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100&is=brand"><b class="multi-icon"></b>风筝牌</a></li>
										<li><a fromtab="spu-brand" brand="64838652" pos="6" title="家萱" href="?cat=50514008&amp;brand=64838652&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100&is=brand"><b class="multi-icon"></b>家萱</a></li>
										<li class="colProp-list-btn">
											<a href="#" title="选择多种品牌" class="entry">选择多种品牌</a>
											<div class="entry-btn">
												<button class="btnSubmit" type="submit">确定</button>
												<a href="#" class="quit ms-toggler" title="取消">取消</a>
											</div>
										</li>

									</ul>
									<a hidefocus="true" class="more close" usuri="//list.tmall.com//ajax/allBrandShowForGaiBanOfChaoshi.htm?cat=50514008&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100"
									 href="#"><b class="icon"></b>更多</a></div>



							</div>

							<input type="hidden" name="q" value="包子">
							<input type="hidden" name="cat" value="50514008">

							<input type="hidden" id="J_PropField" value="">
							<input type="hidden" id="tp_id" value="725677994" name="user_id">
							<input type="hidden" id="start_price" value="" name="start_price">
							<input type="hidden" id="end_price" value="" name="end_price">
						</form>
					</div>
					<!-- 品牌、属性筛选区 end -->

					<!--搜索无结果信息开始-->

					<!--商品列表头部翻页开始-->
					<div class="filter" id="J_Filter">
						<ul class="filter-tab display-settings">
							<li class="selected">商品列表</li>
							<li class="quick-page-changer">
								<span>1/8</span>
								<span class="no-previous"><b class="icon"></b></span>
								<a href="?cat=50514008&amp;s=40&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100#J_Filter"
								 class="next-page">下一页<b class="icon"></b></a>
							</li>
						</ul>
						<section class="mainFilterSearch">
							<form action="/list/search_product.htm" id="filterForm">
								<div class="search-filter clearfix">
									<ul class="filter-toolbar">
										<li class="keyword">
											<label for="filterSearchKeyWord">关键字：<input id="filterSearchKeyWord" type="text" class="text" name="q" size="10" value="包子"/></label>
											<input type="hidden" name="type" value="p" />
											<input type="hidden" name="sort" value="s" />
											<input type="hidden" name="brand" value="" />
											<input type="hidden" name="prop" value="" />
											<input type="hidden" name="user_id" value="725677994" />
											<input type="hidden" name="chaoshi_imported" value="" />
											<input type="hidden" value="50514008" name="cat" id="J_ShopCat">
											<input id="filterCategoryName" type="hidden" value="" name="catName" />
										</li>
										<li class="checkbox"><label for="ku44875125">
<input id="ku44875125" type="checkbox" name="miaosha" value="1" />限时低价</label></li>

										<li class="checkbox"><label for="gc254784112">
 <input id="gc254784112" type="checkbox" name="combo" value="1" />搭配减价</label>
										</li>

										<!--
<li class="checkbox"><label for="ci347532445" >
 <input id="ci347532445" type="checkbox" name="chaoshi_imported" value="1" />进口商品</label>
 </li>
-->


										<!--
<li class="checkbox"><label for="gc254784112">
 <input id="gc254784112" type="checkbox" name="post_fee" value="-1"  />包邮</label></li>
 -->
										<li class="options"><button class="btnSubmit" type="submit">确定</button></li>
									</ul>
									<ul class="filter-sort">
										<li>排序</li>
										<li class="now"><a href="?cat=50514008&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100#J_Filter">默认</a></li>
										<li><a href="?cat=50514008&amp;q=%B0%FC%D7%D3&amp;sort=td&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100#J_Filter"><span>总销量<s></s></span></a></li>
										<li><a href="?cat=50514008&amp;q=%B0%FC%D7%D3&amp;sort=wd&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100#J_Filter"><span>周销量<s></s></span></a></li>
										<li><a class="filter-sort-prices" href="?cat=50514008&amp;q=%B0%FC%D7%D3&amp;sort=p&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100#J_Filter"><span>价格<s></s></span></a></li>
										<li><a href="?cat=50514008&amp;q=%B0%FC%D7%D3&amp;sort=pt&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100#J_Filter"><span>上架时间<s></s></span></a></li>
										<li class="price-order">
											<dl>
												<dt>价格范围：</dt>
												<dd class="by-price">
													<div class="price-range" id="J_FilterPrice">
														<input type="text" class="text" autocomplete="off" name="start_price" size="6" maxlength="8" value="" /> -
														<input type="text" class="text" autocomplete="off" name="end_price" size="6" maxlength="8" value="" />
														<p class="sub-menu">
															<button class="btnSubmit" type="submit">
确定
</button>
															<a href="#" id="J_CancelPriceInput">取消</a>
														</p>
													</div>
												</dd>
											</dl>
										</li>
									</ul>
								</div>
							</form>
						</section>
					</div>
					<!--商品列表形式开始 grid-->
					<div id="J-listContainer" class="mainItemsList">
						<h2 class="offScreen">商品列表</h2>
						<ul id="J_ProductList" class="product-list">



							<li class="product" data-itemid="44607891909">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=44607891909&amp;rewcatid=50514008" target="_blank" atpanel="1,44607891909,50025684,-44607891909,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i1/TB1srIPHpXXXXcfXFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item44607891909Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=44607891909&amp;rewcatid=50514008" target="_blank" atpanel="1,44607891909,50025684,-44607891909,spu,1,spu,">
  【天猫超市】避风塘鲜虾小笼包200g <span class=H>包子</span> 早餐晚餐速食 面食面点
										</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>25464</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>16.90</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=44607891909&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="44607891909" data-pic="//img.alicdn.com/bao/uploaded/i1/TB1srIPHpXXXXcfXFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="1,44607891909,50025684,-44607891909,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="39488853351">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=39488853351&amp;rewcatid=50514008" target="_blank" atpanel="2,39488853351,50025684,-39488853351,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i4/TB1ngTNHpXXXXXRXVXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item39488853351Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=39488853351&amp;rewcatid=50514008" target="_blank" atpanel="2,39488853351,50025684,-39488853351,spu,1,spu,">
  【天猫超市】避风塘香菇菜包（大）350g <span class=H>包子</span> 早餐晚餐速食面食
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>42954</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>12.80</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=39488853351&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="39488853351" data-pic="//img.alicdn.com/bao/uploaded/i4/TB1ngTNHpXXXXXRXVXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="2,39488853351,50025684,-39488853351,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="39498896312">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=39498896312&amp;rewcatid=50514008" target="_blank" atpanel="3,39498896312,50025684,-39498896312,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i3/TB1PxLyHpXXXXa_XFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item39498896312Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=39498896312&amp;rewcatid=50514008" target="_blank" atpanel="3,39498896312,50025684,-39498896312,spu,1,spu,">
  【天猫超市】避风塘叉烧包（大）350g 叉烧<span class=H>包子</span> 冷冻<span class=H>包子</span>
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>52671</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>18.20</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=39498896312&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="39498896312" data-pic="//img.alicdn.com/bao/uploaded/i3/TB1PxLyHpXXXXa_XFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="3,39498896312,50025684,-39498896312,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="549892178029">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=549892178029&amp;rewcatid=50514008" target="_blank" atpanel="4,549892178029,50025684,-549892178029,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i2/TB12bZGQVXXXXbsXpXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item549892178029Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=549892178029&amp;rewcatid=50514008" target="_blank" atpanel="4,549892178029,50025684,-549892178029,spu,1,spu,">
  【天猫超市】狗不理猪肉包420g(12个) <span class=H>包子</span> 传统小食
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>9569</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>17.80</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=549892178029&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="549892178029" data-pic="//img.alicdn.com/bao/uploaded/i2/TB12bZGQVXXXXbsXpXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="4,549892178029,50025684,-549892178029,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="39488713590">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=39488713590&amp;rewcatid=50514008" target="_blank" atpanel="5,39488713590,50025684,-39488713590,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i2/TB1BI2SHpXXXXaPXpXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item39488713590Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=39488713590&amp;rewcatid=50514008" target="_blank" atpanel="5,39488713590,50025684,-39488713590,spu,1,spu,">
  【天猫超市】避风塘香菇菜包（小）210g<span class=H>包子</span> 早餐晚餐速食 面食
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>46999</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>8.50</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=39488713590&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="39488713590" data-pic="//img.alicdn.com/bao/uploaded/i2/TB1BI2SHpXXXXaPXpXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="5,39488713590,50025684,-39488713590,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="522913992712">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=522913992712&amp;rewcatid=50514008" target="_blank" atpanel="6,522913992712,50025684,-522913992712,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i4/TB1nltTKpXXXXbmXFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item522913992712Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=522913992712&amp;rewcatid=50514008" target="_blank" atpanel="6,522913992712,50025684,-522913992712,spu,1,spu,">
  【天猫超市】安井奶黄包360g <span class=H>包子</span> 早餐午餐晚餐 面食 面点 速食
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>14952</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>6.20</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=522913992712&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="522913992712" data-pic="//img.alicdn.com/bao/uploaded/i4/TB1nltTKpXXXXbmXFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="6,522913992712,50025684,-522913992712,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="528045931823">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=528045931823&amp;rewcatid=50514008" target="_blank" atpanel="7,528045931823,50025684,-528045931823,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i3/TB1N_LGLVXXXXcfXVXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item528045931823Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=528045931823&amp;rewcatid=50514008" target="_blank" atpanel="7,528045931823,50025684,-528045931823,spu,1,spu,">
  【天猫超市】五亭三丁包300g（6只） <span class=H>包子</span> 小食 冷冻<span class=H>包子</span>
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>2517</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>13.80</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=528045931823&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="528045931823" data-pic="//img.alicdn.com/bao/uploaded/i3/TB1N_LGLVXXXXcfXVXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="7,528045931823,50025684,-528045931823,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="44983684096">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=44983684096&amp;rewcatid=50514008" target="_blank" atpanel="8,44983684096,50025684,-44983684096,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i4/TB1ps9xHFXXXXcOXpXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item44983684096Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=44983684096&amp;rewcatid=50514008" target="_blank" atpanel="8,44983684096,50025684,-44983684096,spu,1,spu,">
  【天猫超市】龙凤香菇素菜包420g 早餐晚餐<span class=H>包子</span>
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>124912</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>10.90</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=44983684096&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="44983684096" data-pic="//img.alicdn.com/bao/uploaded/i4/TB1ps9xHFXXXXcOXpXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="8,44983684096,50025684,-44983684096,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="528120508446">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=528120508446&amp;rewcatid=50514008" target="_blank" atpanel="9,528120508446,50025684,-528120508446,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i1/TB1W.2vLVXXXXayapXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item528120508446Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=528120508446&amp;rewcatid=50514008" target="_blank" atpanel="9,528120508446,50025684,-528120508446,spu,1,spu,">
  【天猫超市】满66减30思念中华面点奶黄包100g（2只）米妮<span class=H>包子</span>
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>2318</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>26.80</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=528120508446&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="528120508446" data-pic="//img.alicdn.com/bao/uploaded/i1/TB1W.2vLVXXXXayapXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="9,528120508446,50025684,-528120508446,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="549892090019">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=549892090019&amp;rewcatid=50514008" target="_blank" atpanel="10,549892090019,50025684,-549892090019,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i1/TB1k6oIQVXXXXXYXpXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item549892090019Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=549892090019&amp;rewcatid=50514008" target="_blank" atpanel="10,549892090019,50025684,-549892090019,spu,1,spu,">
  【天猫超市】狗不理三鲜包420g(12只) <span class=H>包子</span> 传统小食
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>4880</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>18.80</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=549892090019&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="549892090019" data-pic="//img.alicdn.com/bao/uploaded/i1/TB1k6oIQVXXXXXYXpXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="10,549892090019,50025684,-549892090019,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="549963307340">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=549963307340&amp;rewcatid=50514008" target="_blank" atpanel="11,549963307340,50025684,-549963307340,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i2/TB1lX7PQVXXXXcrXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item549963307340Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=549963307340&amp;rewcatid=50514008" target="_blank" atpanel="11,549963307340,50025684,-549963307340,spu,1,spu,">
  【天猫超市】狗不理猪肉野菜包420g(12个) <span class=H>包子</span> 传统小食
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>2437</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>19.20</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=549963307340&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="549963307340" data-pic="//img.alicdn.com/bao/uploaded/i2/TB1lX7PQVXXXXcrXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="11,549963307340,50025684,-549963307340,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="549869345772">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=549869345772&amp;rewcatid=50514008" target="_blank" atpanel="12,549869345772,50025684,-549869345772,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i2/TB1BRwoQVXXXXbEXFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item549869345772Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=549869345772&amp;rewcatid=50514008" target="_blank" atpanel="12,549869345772,50025684,-549869345772,spu,1,spu,">
  【天猫超市】狗不理猪肉韭菜包420g(12个) <span class=H>包子</span> 传统小食
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>2027</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>17.80</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=549869345772&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="549869345772" data-pic="//img.alicdn.com/bao/uploaded/i2/TB1BRwoQVXXXXbEXFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="12,549869345772,50025684,-549869345772,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="549962947550">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=549962947550&amp;rewcatid=50514008" target="_blank" atpanel="13,549962947550,50025684,-549962947550,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i4/TB1JSwrQVXXXXaJXFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item549962947550Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=549962947550&amp;rewcatid=50514008" target="_blank" atpanel="13,549962947550,50025684,-549962947550,spu,1,spu,">
  【天猫超市】狗不理酱肉包420g(12个) <span class=H>包子</span> 传统小食
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>3692</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>18.80</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=549962947550&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="549962947550" data-pic="//img.alicdn.com/bao/uploaded/i4/TB1JSwrQVXXXXaJXFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="13,549962947550,50025684,-549962947550,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="549869605526">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=549869605526&amp;rewcatid=50514008" target="_blank" atpanel="14,549869605526,50025684,-549869605526,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i2/TB19a_6QVXXXXbSapXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item549869605526Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=549869605526&amp;rewcatid=50514008" target="_blank" atpanel="14,549869605526,50025684,-549869605526,spu,1,spu,">
  【天猫超市】狗不理素包420g(12个) <span class=H>包子</span> 传统小食
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>2544</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>17.80</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=549869605526&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="549869605526" data-pic="//img.alicdn.com/bao/uploaded/i2/TB19a_6QVXXXXbSapXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="14,549869605526,50025684,-549869605526,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="528045779924">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=528045779924&amp;rewcatid=50514008" target="_blank" atpanel="15,528045779924,50025684,-528045779924,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i4/TB1ezrKLVXXXXb2XFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item528045779924Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=528045779924&amp;rewcatid=50514008" target="_blank" atpanel="15,528045779924,50025684,-528045779924,spu,1,spu,">
  【天猫超市】五亭梅干菜包300g（6只） <span class=H>包子</span> 冷冻<span class=H>包子</span>
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>20449</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>13.80</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=528045779924&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="528045779924" data-pic="//img.alicdn.com/bao/uploaded/i4/TB1ezrKLVXXXXb2XFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="15,528045779924,50025684,-528045779924,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="554875259957">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=554875259957&amp;rewcatid=50514008" target="_blank" atpanel="16,554875259957,50025684,-554875259957,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i4/TB1xw9VSXXXXXXfXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item554875259957Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=554875259957&amp;rewcatid=50514008" target="_blank" atpanel="16,554875259957,50025684,-554875259957,spu,1,spu,">
  【天猫超市】狗不理猪肉白菜包420g(12个)  <span class=H>包子</span> 传统小食
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>1092</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>17.80</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=554875259957&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="554875259957" data-pic="//img.alicdn.com/bao/uploaded/i4/TB1xw9VSXXXXXXfXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="16,554875259957,50025684,-554875259957,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="528120528577">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=528120528577&amp;rewcatid=50514008" target="_blank" atpanel="17,528120528577,50025684,-528120528577,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i1/TB1zs63LVXXXXXHXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item528120528577Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=528120528577&amp;rewcatid=50514008" target="_blank" atpanel="17,528120528577,50025684,-528120528577,spu,1,spu,">
  【天猫超市】思念中华面点豆沙包100g（2只）米奇造型 冷冻<span class=H>包子</span>
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>1482</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>16.90</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=528120528577&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="528120528577" data-pic="//img.alicdn.com/bao/uploaded/i1/TB1zs63LVXXXXXHXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="17,528120528577,50025684,-528120528577,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="44983332753">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=44983332753&amp;rewcatid=50514008" target="_blank" atpanel="18,44983332753,50025684,-44983332753,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i4/TB11XGmHFXXXXc2XVXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item44983332753Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=44983332753&amp;rewcatid=50514008" target="_blank" atpanel="18,44983332753,50025684,-44983332753,spu,1,spu,">
  【天猫超市】龙凤猪肉包420g
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>33895</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>11.50</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=44983332753&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="44983332753" data-pic="//img.alicdn.com/bao/uploaded/i4/TB11XGmHFXXXXc2XVXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="18,44983332753,50025684,-44983332753,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="45597210082">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45597210082&amp;rewcatid=50514008" target="_blank" atpanel="19,45597210082,124226015,345240652,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i4/TB15VJMRpXXXXcJXFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item45597210082Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45597210082&amp;rewcatid=50514008" target="_blank" atpanel="19,45597210082,124226015,345240652,spu,1,spu,">
  【天猫超市】安琪 高活性干酵母 5g/袋 制作<span class=H>包子</span>馒头饼麻花等
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>2471365</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>0.50</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45597210082&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="45597210082" data-pic="//img.alicdn.com/bao/uploaded/i4/TB15VJMRpXXXXcJXFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="19,45597210082,124226015,345240652,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="535583068992">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=535583068992&amp;rewcatid=50514008" target="_blank" atpanel="20,535583068992,50009839,282545417,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i4/TB12lLVQVXXXXaDXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item535583068992Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=535583068992&amp;rewcatid=50514008" target="_blank" atpanel="20,535583068992,50009839,282545417,spu,1,spu,">
  【天猫超市】新良馒头自发粉2.5KG 馒头自发粉<span class=H>包子</span>小麦面粉
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>14393</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>25.80</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=535583068992&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="535583068992" data-pic="//img.alicdn.com/bao/uploaded/i4/TB12lLVQVXXXXaDXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="20,535583068992,50009839,282545417,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="40339483836">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=40339483836&amp;rewcatid=50514008" target="_blank" atpanel="21,40339483836,50009839,288482733,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i1/TB10qlRGVXXXXXbXpXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item40339483836Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=40339483836&amp;rewcatid=50514008" target="_blank" atpanel="21,40339483836,50009839,288482733,spu,1,spu,">
  【天猫超市】风筝面粉 中筋小麦粉2.5kg <span class=H>包子</span>馒头饼 白面 烘焙
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>43438</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>22.90</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=40339483836&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="40339483836" data-pic="//img.alicdn.com/bao/uploaded/i1/TB10qlRGVXXXXXbXpXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="21,40339483836,50009839,288482733,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="531284038292">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=531284038292&amp;rewcatid=50514008" target="_blank" atpanel="22,531284038292,50009839,569511415,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i4/TB1hiK_SpXXXXaUXFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item531284038292Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=531284038292&amp;rewcatid=50514008" target="_blank" atpanel="22,531284038292,50009839,569511415,spu,1,spu,">
  【天猫超市】安琪 百钻中筋小麦粉 500g <span class=H>包子</span>馒头饺子面条面粉
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>22194</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>4.99</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=531284038292&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="531284038292" data-pic="//img.alicdn.com/bao/uploaded/i4/TB1hiK_SpXXXXaUXFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="22,531284038292,50009839,569511415,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="523246855323">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=523246855323&amp;rewcatid=50514008" target="_blank" atpanel="23,523246855323,50009839,306680042,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i3/TB1YLJDRXXXXXbDaXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item523246855323Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=523246855323&amp;rewcatid=50514008" target="_blank" atpanel="23,523246855323,50009839,306680042,spu,1,spu,">
  【天猫超市】中裕雪花粉（蒸）2kg <span class=H>包子</span>馒头面粉面食 雪花小麦粉
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>19746</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>59.80</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=523246855323&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="523246855323" data-pic="//img.alicdn.com/bao/uploaded/i3/TB1YLJDRXXXXXbDaXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="23,523246855323,50009839,306680042,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="528950569133">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=528950569133&amp;rewcatid=50514008" target="_blank" atpanel="24,528950569133,50025791,522717901,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i2/TB1xxuFSpXXXXazaXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item528950569133Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=528950569133&amp;rewcatid=50514008" target="_blank" atpanel="24,528950569133,50025791,522717901,spu,1,spu,">
  【天猫超市】家萱蒸笼布蒸饺布蒸笼纱布<span class=H>包子</span>馒头垫俩片装抹布6072
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>44958</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>9.90</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=528950569133&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="528950569133" data-pic="//img.alicdn.com/bao/uploaded/i2/TB1xxuFSpXXXXazaXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="24,528950569133,50025791,522717901,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="45824172227">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45824172227&amp;rewcatid=50514008" target="_blank" atpanel="25,45824172227,50025684,-45824172227,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i2/TB1S_x8HVXXXXbhXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item45824172227Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45824172227&amp;rewcatid=50514008" target="_blank" atpanel="25,45824172227,50025684,-45824172227,spu,1,spu,">
  【天猫超市】安井手抓饼（原味）900g
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>595849</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>19.90</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45824172227&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="45824172227" data-pic="//img.alicdn.com/bao/uploaded/i2/TB1S_x8HVXXXXbhXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="25,45824172227,50025684,-45824172227,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="44921078244">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=44921078244&amp;rewcatid=50514008" target="_blank" atpanel="26,44921078244,50025684,-44921078244,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i1/TB1kSW7NXXXXXblXpXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item44921078244Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=44921078244&amp;rewcatid=50514008" target="_blank" atpanel="26,44921078244,50025684,-44921078244,spu,1,spu,">
  【天猫超市】龙凤煎饺900g 饺子小吃 午餐晚餐 速食
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>286160</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>15.90</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=44921078244&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="44921078244" data-pic="//img.alicdn.com/bao/uploaded/i1/TB1kSW7NXXXXXblXpXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="26,44921078244,50025684,-44921078244,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="39469182865">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=39469182865&amp;rewcatid=50514008" target="_blank" atpanel="27,39469182865,50025684,-39469182865,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i3/TB1yB2wHpXXXXaXapXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item39469182865Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=39469182865&amp;rewcatid=50514008" target="_blank" atpanel="27,39469182865,50025684,-39469182865,spu,1,spu,">
  【天猫超市】避风塘虾饺150g 午餐晚餐 面食面点速食
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>176067</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>20.60</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=39469182865&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="39469182865" data-pic="//img.alicdn.com/bao/uploaded/i3/TB1yB2wHpXXXXaXapXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="27,39469182865,50025684,-39469182865,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="45824032402">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45824032402&amp;rewcatid=50514008" target="_blank" atpanel="28,45824032402,50025684,-45824032402,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i2/TB1S_x8HVXXXXbhXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item45824032402Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45824032402&amp;rewcatid=50514008" target="_blank" atpanel="28,45824032402,50025684,-45824032402,spu,1,spu,">
  【天猫超市】安井手抓饼（葱香）900g
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>182466</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>19.90</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45824032402&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="45824032402" data-pic="//img.alicdn.com/bao/uploaded/i2/TB1S_x8HVXXXXbhXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="28,45824032402,50025684,-45824032402,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="45823844939">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45823844939&amp;rewcatid=50514008" target="_blank" atpanel="29,45823844939,50025684,-45823844939,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i2/TB1S_x8HVXXXXbhXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item45823844939Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45823844939&amp;rewcatid=50514008" target="_blank" atpanel="29,45823844939,50025684,-45823844939,spu,1,spu,">
  【天猫超市】安井手抓饼（原味）2250g
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>49210</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>33.50</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45823844939&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="45823844939" data-pic="//img.alicdn.com/bao/uploaded/i2/TB1S_x8HVXXXXbhXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="29,45823844939,50025684,-45823844939,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="45803977040">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45803977040&amp;rewcatid=50514008" target="_blank" atpanel="30,45803977040,50025684,-45803977040,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i2/TB1S_x8HVXXXXbhXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item45803977040Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45803977040&amp;rewcatid=50514008" target="_blank" atpanel="30,45803977040,50025684,-45803977040,spu,1,spu,">
  【天猫超市】安井手抓饼（葱香）2250g
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>26686</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>33.50</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45803977040&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="45803977040" data-pic="//img.alicdn.com/bao/uploaded/i2/TB1S_x8HVXXXXbhXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="30,45803977040,50025684,-45803977040,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="45760806670">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45760806670&amp;rewcatid=50514008" target="_blank" atpanel="31,45760806670,50025684,-45760806670,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i4/TB1zP2DIXXXXXcwXpXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item45760806670Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45760806670&amp;rewcatid=50514008" target="_blank" atpanel="31,45760806670,50025684,-45760806670,spu,1,spu,">
  【天猫超市】龙凤1300g奶黄包
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>41625</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>22.80</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45760806670&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="45760806670" data-pic="//img.alicdn.com/bao/uploaded/i4/TB1zP2DIXXXXXcwXpXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="31,45760806670,50025684,-45760806670,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="542973355785">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=542973355785&amp;rewcatid=50514008" target="_blank" atpanel="32,542973355785,50009839,714133419,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i4/TB1.xJERXXXXXaHXFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item542973355785Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=542973355785&amp;rewcatid=50514008" target="_blank" atpanel="32,542973355785,50009839,714133419,spu,1,spu,">
  【天猫超市】安琪干酵母粉15g*5包高活性即发<span class=H>包子</span>馒头面包发酵粉
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>5155</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>7.90</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=542973355785&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="542973355785" data-pic="//img.alicdn.com/bao/uploaded/i4/TB1.xJERXXXXXaHXFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="32,542973355785,50009839,714133419,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="16482476765">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=16482476765&amp;rewcatid=50514008" target="_blank" atpanel="33,16482476765,50009839,268961194,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i4/TB1ZAsAHXXXXXa.XVXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item16482476765Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=16482476765&amp;rewcatid=50514008" target="_blank" atpanel="33,16482476765,50009839,268961194,spu,1,spu,">
  【天猫超市】风筝面粉 特一粉1kg 白面烘焙<span class=H>包子</span>馒头饼 特质一等粉
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>159234</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>8.40</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=16482476765&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="16482476765" data-pic="//img.alicdn.com/bao/uploaded/i4/TB1ZAsAHXXXXXa.XVXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="33,16482476765,50009839,268961194,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="45628762956">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45628762956&amp;rewcatid=50514008" target="_blank" atpanel="34,45628762956,50025684,-45628762956,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i3/TB1rJlZKVXXXXXVXVXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item45628762956Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45628762956&amp;rewcatid=50514008" target="_blank" atpanel="34,45628762956,50025684,-45628762956,spu,1,spu,">
  【天猫超市】龙凤红豆包1.3kg
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>35343</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>18.50</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45628762956&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="45628762956" data-pic="//img.alicdn.com/bao/uploaded/i3/TB1rJlZKVXXXXXVXVXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="34,45628762956,50025684,-45628762956,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="45803329999">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45803329999&amp;rewcatid=50514008" target="_blank" atpanel="35,45803329999,50025684,-45803329999,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i1/TB1R_QcIXXXXXbzXFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item45803329999Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45803329999&amp;rewcatid=50514008" target="_blank" atpanel="35,45803329999,50025684,-45803329999,spu,1,spu,">
  【天猫超市】安井红糖馒头800g 冷冻馒头
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>40600</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>15.90</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=45803329999&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="45803329999" data-pic="//img.alicdn.com/bao/uploaded/i1/TB1R_QcIXXXXXbzXFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="35,45803329999,50025684,-45803329999,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="44983236891">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=44983236891&amp;rewcatid=50514008" target="_blank" atpanel="36,44983236891,50025684,-44983236891,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i3/TB1jLynKVXXXXbwXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item44983236891Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=44983236891&amp;rewcatid=50514008" target="_blank" atpanel="36,44983236891,50025684,-44983236891,spu,1,spu,">
  【天猫超市】龙凤奶黄包420g 方便速冻面食早餐晚餐
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>289419</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>9.90</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=44983236891&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="44983236891" data-pic="//img.alicdn.com/bao/uploaded/i3/TB1jLynKVXXXXbwXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="36,44983236891,50025684,-44983236891,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="520959489436">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=520959489436&amp;rewcatid=50514008" target="_blank" atpanel="37,520959489436,50025684,-520959489436,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i3/TB1by_DIVXXXXbeXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item520959489436Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=520959489436&amp;rewcatid=50514008" target="_blank" atpanel="37,520959489436,50025684,-520959489436,spu,1,spu,">
  【天猫超市】思念放心油条900g
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>85396</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>18.00</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=520959489436&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="520959489436" data-pic="//img.alicdn.com/bao/uploaded/i3/TB1by_DIVXXXXbeXXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="37,520959489436,50025684,-520959489436,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="39469166904">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=39469166904&amp;rewcatid=50514008" target="_blank" atpanel="38,39469166904,50025684,-39469166904,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i1/TB1jD2FHpXXXXcoXFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item39469166904Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=39469166904&amp;rewcatid=50514008" target="_blank" atpanel="38,39469166904,50025684,-39469166904,spu,1,spu,">
  【天猫超市】避风塘鲜肉糯米烧卖240g
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>265840</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>9.90</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=39469166904&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="39469166904" data-pic="//img.alicdn.com/bao/uploaded/i1/TB1jD2FHpXXXXcoXFXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="38,39469166904,50025684,-39469166904,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="528192007143">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=528192007143&amp;rewcatid=50514008" target="_blank" atpanel="39,528192007143,50009839,520418293,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i2/TB1iDFzSFXXXXXNXVXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item528192007143Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=528192007143&amp;rewcatid=50514008" target="_blank" atpanel="39,528192007143,50009839,520418293,spu,1,spu,">
  【天猫超市】安琪干酵母粉15g高活性即发<span class=H>包子</span>馒头面包发酵粉
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>85695</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>1.90</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=528192007143&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="528192007143" data-pic="//img.alicdn.com/bao/uploaded/i2/TB1iDFzSFXXXXXNXVXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="39,528192007143,50009839,520418293,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>



							<li class="product" data-itemid="44921010385">
								<div class="productInfo">
									<div class="product-img">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=44921010385&amp;rewcatid=50514008" target="_blank" atpanel="40,44921010385,50025684,-44921010385,spu,1,spu,"><img src="//img.alicdn.com/bao/uploaded/i3/TB1OBGiHFXXXXbaaXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg" id="J_Item44921010385Pic"></a>
									</div>


									<h3 class="product-title">
										<a href="//chaoshi.detail.tmall.com/item.htm?id=44921010385&amp;rewcatid=50514008" target="_blank" atpanel="40,44921010385,50025684,-44921010385,spu,1,spu,">
  【天猫超市】龙凤牛奶馒头400g  方便速冻面食传统糕点
</a>
									</h3>
									<div class="item-summary">
										<div class="item-sum">
											<span>总销量:</span>
											<strong>294556</strong>
										</div>
										<div class="item-price">
											<span class="ui-price">
 <span class="price-icon">&yen;</span>
											<strong>6.90</strong>
											</span>
										</div>
										<a href="//chaoshi.detail.tmall.com/item.htm?id=44921010385&rewcatid=50514008" target="_blank" class="addCart j_AddCart"
										 data-itemid="44921010385" data-pic="//img.alicdn.com/bao/uploaded/i3/TB1OBGiHFXXXXbaaXXXXXXXXXXX_!!0-item_pic.jpg_160x160.jpg"
										 atpanel="40,44921010385,50025684,-44921010385,cart,1,cart,">&#xe600;</a>
									</div>

								</div>
							</li>
						</ul>
					</div>

					<!--商品列表页尾翻页开始-->
					<div class="list-bottom">

						<div class="pagination mb20">
							<div class="page-bottom"> <span class="page-start"><b class="icon"></b>上一页</span>
								<span class="page-cur">1</span>
								<a href="?cat=50514008&amp;s=40&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100#J_Filter">2</a>
								<a href="?cat=50514008&amp;s=80&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100#J_Filter">3</a>
								<a href="?cat=50514008&amp;s=120&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100#J_Filter">4</a>
								<a href="?cat=50514008&amp;s=160&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100#J_Filter">5</a>
								<span class="page-break">...</span>
								<a class="page-next" href="?cat=50514008&amp;s=40&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100#J_Filter">下一页<b class="icon"></b></a>
								<span class="page-skip">
 <form id="filterPageForm" name="filterPageForm" method="get" action="?cat=50514008&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100">
 <input type="hidden" name="totalPage" id="totalPage" value="8"/>
 <input type="hidden" name="q" id="q" value="包子">
 <input type="hidden" name="sort" value="s"/>
 <input type="hidden" name="user_id" value="725677994"/>
 <input type="hidden" name="style" value="g"/>
 <input type="hidden" name="brand" value=""/>
 <input type="hidden" name="prop" value=""/>
 <input type="hidden" name="start_price" value=""/>
 <input type="hidden" name="end_price" value=""/>
<input type="hidden" name="chaoshi_imported" value=""/>
 <input type="hidden" name="cat" value="50514008"/>
 共8页，到第<input id="jumpto" type="text" name="jumpto" class="pageSkip-jumpto" size="3" value="1" data-max="8">页
 <button type="submit" class="pageSkip-search">确定</button>
 </form>
 </span>
							</div>
						</div>
					</div>
				</div>
			</div>

			<div class="side">
				<div class="category">
					<div class="hd">
						<h3>

							<a href="//list.tmall.com/search_product.htm?cat=50514008&user_id=725677994&search_condition=1&style=g&q=%B0%FC%D7%D3#J_crumbs">所有类目</a>

						</h3>
					</div>

					<div class="bd">



						<ul id="J_Tree" data-url="/ajax/getSubCatsOfChaoshi.htm" data-param="q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100">



							<li class="collapse" data-param="cat=50514009">

								<a href="?cat=50514009&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100">
粮油/米面/速食</a>

							</li>

							<li class="collapse" data-param="cat=52598012">

								<a href="?cat=52598012&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100">
生鲜水果</a>

							</li>

							<li class="collapse" data-param="cat=51454011">

								<a href="?cat=51454011&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100">
进口商品</a>

							</li>

							<li class="collapse" data-param="cat=50518004">

								<a href="?cat=50518004&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100">
清洁剂/清洁工具</a>

							</li>

							<li class="collapse" data-param="cat=50520007">

								<a href="?cat=50520007&amp;q=%B0%FC%D7%D3&amp;sort=s&amp;style=g&amp;user_id=725677994&amp;from=chaoshi..pc_1_searchbutton&amp;industryCatId=50514008&amp;spm=a3204.7933263.a2227oh.d100&amp;smAreaId=310100">
锅具/刀具/水具/餐具</a>

							</li>




						</ul>



					</div>





				</div>

				<div id="chaoshiRecommend"></div>
			</div>
			<script>
				var __list_atpanel_param = "rn=7fc97be1a643f68eb11af46ce63620c1&q=%B0%FC%D7%D3&bid=3&uid=moonhmilyms&catid=50514008&prop=&sort=s&disp=g&filter=&loc=&n=40&page=1&v=mall_1.0&vmarket=0&machineid=1ae9652d4118a5fead2d37b13c1948a1&tmalltrackid=login.tmall.com&nav=&navlog=&rewq=%B0%FC%D7%D3&rewcatid=50514008&page_type=1&stats=qp:1|cat:1|brand:1|brand-qp:1|F.itag:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0|userloc:310100|key:1|querytype:256|skuahead:2|itemPage:1|defaultsearch:1|sellersort:1|app:tmallsearchquery|vmarket:chaoshi|industryId:311|industryId:357|industryId:455|industryId:533|industryId:534|industryId:537|industryId:608|initiative:1&filter_new=sort:s|post_fee:0|support_cod:0|manyPoints:0|wwonline:0|miaosha:0|isCombo:0|vip:0|pic_detail:0|floc:0|fprice:0|new:0|filter_mj:0&from=chaoshi..pc_1_searchbutton&active=0&wq=&suggest=&search_type=search&abtest=&std_query=%B0%FC%D7%D3&top_query=&direct_rc=50514008&userid=667497065&cna=SgNYEVNBm18CAbSfNyjAtokF&",
					__header_atpanel_param = "bid=3&rn=7fc97be1a643f68eb11af46ce63620c1";
			</script>
		</div>
	</div>
	<div id="footer" data-spm="a2226n1" class="tm-chn-chaoshi-footer ">

		<div id="tmall-desc">
			<style>
				@media (max-width: 1280px) {
					#tmall-ensure {
						width: 990px !important;
						background-image: url(//img.alicdn.com/tps/i2/T1vYemFC0eXXcnC4Lh-990-100.jpg)
					}

					#tmall-ensure a {
						width: 247px
					}

					#tmall-desc {
						width: 990px !important;
						background-position: 12px bottom;
					}

					#tmall-desc dl {
						padding-left: 15px;
						width: 200px
					}

					#tmall-desc #mobile {
						width: 110px
					}

					#tmall-copyright .footer-tmallinfo,
					#tmall-copyright .footer-otherlink,
					#tmall-copyright .footer-copyright {
						width: 990px
					}
				}
			</style>
			<img src="//img.alicdn.com/tps/i2/TB1ijJ1HFXXXXayXVXXFq5g_FXX-112-40.png" class="logo" />
			<dl id="beginner">
				<dt><span><a href="//www.tmall.com/wow/chaoshi/act/help-gouwuzhinan?spm=a312d.7832034.0.0.Fe3sLx">购物指南</a></span></dt>
				<dd>
					<a href="//www.tmall.com/wow/chaoshi/act/help-gouwuzhinan?spm=a312d.7832034.0.0.Fe3sLx#dh1" target="_blank"><i></i>购物流程</a>
					<a class="chaoshi-highlight" href="//service.tmall.com/support/tmall/knowledge-1137790.htm?spm=a3204.7843358.5906693.23.CIA5Jh"><i></i>配送时效说明</a>
					<a class="chaoshi-highlight" href="//service.tmall.com/support/tmall/knowledge-1137790.htm?spm=a3204.7843358.5906693.23.CIA5Jh"><i></i>配送区域及费用</a>
					<a class="chaoshi-highlight" href="//service.tmall.com/support/tmall/knowledge-5695577.htm" target="_blank"><i></i>购买生鲜须知</a>
					<a href="//service.tmall.com/support/tmall/knowledge-5529465.htm?spm=a3204.7843358.5906693.28.s3noiz" target="_blank"><i></i>发票流程</a>
				</dd>
			</dl>
			<dl id="saleservice">
				<dt><span><a href="//www.tmall.com/wow/chaoshi/act/help-shouhoufuwu?spm=a3204.7843358.5906693.8.pmRqaP">售后服务</a></span></dt>
				<dd>
					<a href="//service.tmall.com/support/tmall/knowledge-1137792.htm?spm=a3204.7843371.5906693.9.qfbQpn" target="_blank"><i></i>退货规则</a>
					<a href="//www.tmall.com/wow/chaoshi/act/help-shouhoufuwu?spm=a3204.7843358.5906693.8.pmRqaP#dh3" target="_blank"><i></i>退货指南</a>
					<a href="//service.tmall.com/support/tmall/knowledge-5415346.htm" target="_blank"><i></i>保质期说明</a>
					<a href="//service.tmall.com/support/tmall/knowledge-5650874.htm" target="_blank" style="white-space: nowrap;width: 103px;"><i></i>联系客服</a>
				</dd>
			</dl>
			<dl id="payment">
				<dt><span><a href="//www.tmall.com/wow/chaoshi/act/help-zizhufuwu?spm=a3204.7843371.5906693.13.wz4NsW">自助服务</a></span></dt>
				<dd>
					<a href="//trade.taobao.com/trade/itemlist/list_bought_items.htm" target="_blank"><i></i>订单物流查询</a>
					<a href="//chaoshi.tmall.com/cart/my_cart.htm?spm=3.405264.0.791.Bg1frD&tp_id=725677994" target="_blank"><i></i>我的购物车</a>
					<a href="//ecrm.taobao.com/mallcoupon/got_bonus.htm?spm=a1z09.2.a2109.d1000376.pIvZYG&nekot=1366359455986" target="_blank"><i></i>我的现金券</a>
					<a href="//service.tmall.com/support/tmall/knowledge-5529466.htm" target="_blank"><i></i>购物常见问题</a>
					<a class="chaoshi-highlight" href="//feedback.taobao.com/pc/feedbacks?productId=335&source=chaoshi.tmall" target="_blank"><i></i>建议反馈</a>
				</dd>
			</dl>

			<dl id="about">
				<dt><span><a href="//www.tmall.com/wow/chaoshi/act/help-shangjiafuwu?spm=a3204.7843387.5906693.19.Wzlo6D">商家服务</a></span></dt>
				<dd>
					<a href="//service.tmall.com/support/tmall/knowledge-1137800.htm" target="_blank"><i></i>关于天猫超市</a>
					<a class="chaoshi-highlight" href="//www.tmall.com/wow/chaoshi/act/chaoshi-rjru" target="_blank"><i></i>入驻天猫超市</a>
					<a href="//www.tmall.com/wow/chaoshi/act/help-shangjiafuwu?spm=a3204.7843387.5906693.19.Wzlo6D#dh3" target="_blank"><i></i>商家常见问题</a>
				</dd>
			</dl>

			<dl class="tmall-mobile" id="mobile">
				<dt>随时随地逛</dt>
				<dd>
					<a href="//chaoshi.m.tmall.com/" class="join"><img src="//gtms03.alicdn.com/tps/i3/T1zuSAFRJbXXaSJVsE-115-115.png" alt="随时随地逛"/></a>
				</dd>
			</dl>
		</div>
		<div id="tmall-copyright">
			<div class="mui-global-fragment-load" data-fragment="tmbase/mui_footer_link"></div>
		</div>
		<div id="server-num">tmallsearch011139173082.unzbyun.na61</div>
	</div>
	</div>


	<script type="text/javascript">
				setTimeout(function () {
					if (window.goldlog && window.goldlog.record) {
						window.goldlog.record('/mallsearch.expo.page', 'EXP', window.__list_atpanel_param || '', 'H1477801390');
					}
				}, 3000);
	</script>
</body>

</html>

'''
page = BeautifulSoup(html, 'html.parser')
product_ul = page.find(id='J_ProductList').children
products = []
skip = 1
limit = 5

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



# if __name__ == '__main__':
#     printkw(456)
