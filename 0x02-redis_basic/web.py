#!/usr/bin/env python3
""" getting page via url given and return count if access trials"""
import requests
import redis
from functools import wraps

r = redis.Redis()


def cache_page(func):
    """decorator for counting access number"""
    @wraps(func)
    def wrapper(url: str) -> str:
        """wrapper method"""
        cache_key = f"page:{url}"
        count_key = f"count:{url}"

        r.incr(count_key)
        cached_page = r.get(cache_key)
        if cached_page:
            print("Returning cached content")
            return cached_page.decode('utf-8')
        content = func(url)
        r.setex(cache_key, 10, content)
        return content
    return wrapper


@cache_page
def get_page(url: str) -> str:
    """method to get html of page via url"""
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
