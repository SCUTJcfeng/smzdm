
import json

# 搜索
SEARCH_API = 'https://api.smzdm.com/v1/list?keyword={}&category_id=&brand_id=&mall_id=&order=time&limit={}&offset={}'

# 好价
HAOJIA_API = 'https://api.smzdm.com/v1/common/list_data'

# 首页
# MAIN_API = 'https://homepage-api.smzdm.com/v1/home?tab_id=0&device_id=&smzdm_id=&page=1&limit=20&time_sort=&update_timestamp=&past_num=0&is_show_guide=&widget_id=&ad_info=&refresh=1&recfeed_switch=1&haojia_title_abtest=b'


def build_search_url(keyword, limit=10, offset=0):
    return SEARCH_API.format(keyword, limit, offset)


def build_haojia_url(keyword):
    params = {
        'params': {'common_type': 1},
        'tab_params': {'tab': 'haojia', 'channel': 'haojia', 'keyword': keyword, 'keyword_type': 'category'},
        'filter_params': {'filter': 'faxian'},
        'page': 1
    }
    return HAOJIA_API + '?' + '&'.join((k + "=" + json.dumps(v) for k, v in params.items()))
