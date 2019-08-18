
from utils.http import HttpClient
from analysis import keyword_analysis, haojia_analysis
from api import build_search_url, build_haojia_url
from config import KEYWORD_MAP, HAOJIA_MAP


def handler_keyword():
    for keyword, maps in KEYWORD_MAP.items():
        data = HttpClient.get_json(build_search_url(keyword))
        keyword_analysis(data, maps)


def handler_haojia():
    for keyword, maps in HAOJIA_MAP.items():
        data = HttpClient.get_json(build_haojia_url(keyword))
        haojia_analysis(data, maps)
