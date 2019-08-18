
import traceback
import requests

from api import build_search_url
from config import KEYWORD_MAP
from analysis import keyword_analysis


def handler_keyword():
    for keyword, maps in KEYWORD_MAP.items():
        try:
            data = requests.get(build_search_url(keyword)).json()
            keyword_analysis(data, maps)
        except:
            traceback.print_exc()
