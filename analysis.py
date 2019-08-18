

import datetime
from notify import notify_wx


def keyword_analysis(data, maps):
    for sku_data in data['data']['rows']:
        article_url = sku_data['article_url']
        article_title = sku_data['article_title']
        article_mall = sku_data.get('article_mall')
        article_price = sku_data.get('article_price')
        publish_date_lt = sku_data['publish_date_lt']
        print('---搜索', article_title, article_url, article_mall, article_price, publish_date_lt)
        if not is_time_valid(publish_date_lt):
            continue
        if not is_match(article_title.upper(), maps):
            continue
        notify_wx(format_msg(article_title, article_url, article_mall, article_price))


def haojia_analysis(data, maps):
    for sku_data in data['data']['rows']:
        article_url = sku_data['article_url']
        article_title = sku_data['article_title']
        article_mall = sku_data.get('article_mall')
        article_price = sku_data.get('article_price')
        time_sort = sku_data['time_sort']
        print('---好价', article_title, article_url, article_mall, article_price, time_sort)
        publish_time = datetime.datetime.strptime(time_sort, "%Y-%m-%d %H:%M:%S").timestamp()
        if not is_time_valid(publish_time):
            continue
        if not is_match(article_title.upper(), maps):
            continue
        notify_wx(format_msg(article_title, article_url, article_mall, article_price))


def is_time_valid(time_int):
    now = int(datetime.datetime.now().timestamp())
    if (now - int(time_int)) > 60 * 30:
        return False
    return True


def is_match(title, maps):
    def is_keyword_match(title, keyword_list):
        for keyword in keyword_list:
            if keyword not in title:
                return False
        return True

    for keyword_list in maps:
        if is_keyword_match(title, keyword_list):
            return True
    return False


def format_msg(title, url, mall, price):
    return f'标题: {title}\n' \
        f'地址: {url}\n' \
        f'来源: {mall}\n' \
        f'价格: {price}'
