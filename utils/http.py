
import requests
import traceback


class HttpClient:

    @staticmethod
    def get_json(url):
        try:
            return requests.get(url, timeout=20).json()
        except:
            traceback.print_exc()
        return {}
