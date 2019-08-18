

import datetime


def keyword_analysis(data, maps):
    for sku_data in data['data']['rows']:
        article_url = sku_data['article_url']
        article_title = sku_data['article_title']
        article_mall = sku_data['article_mall']
        article_price = sku_data['article_price']
        publish_date_lt = sku_data['publish_date_lt']
        print(article_title, article_url, article_mall, article_price, publish_date_lt)
        if not is_time_valid(publish_date_lt):
            continue
        if not is_match(article_title.upper(), maps):
            continue
        notify(format_msg(article_title, article_url, article_mall, article_price))


def is_time_valid(time_int):
    now = int(datetime.datetime.now().timestamp())
    if (now - int(time_int)) > 60 * 5:
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


def notify(msg):
    print(msg)
