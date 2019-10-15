#!/usr/bin/python3

from lib import log
import json
import time
import requests


logger = log.get_logger("http_request.core")
default_headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/74.0.3729.169 Safari/537.36"
}
ml_headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
}


def html_get(url, headers=None):
    # if set none, use default headers
    if headers is None:
        headers = default_headers
    try:
        r = requests.get(url, headers=headers, timeout=30)
        if r.status_code == 200:
            return r.content
        else:
            print("Error response code: " + str(r.status_code))

    except requests.exceptions.HTTPError:
        print("Http error, retry")
    except requests.exceptions.ConnectionError:
        print("Connection error, retry")
        return html_get(url, headers)
    except requests.exceptions.Timeout:
        print("Request timeout, retry")
        time.sleep(1)
        return html_get(url, headers)
    except requests.exceptions.RequestException:
        print("Something else error, retry")


def api_get(url, headers=None):
    # if set none, use default headers
    if headers is None:
        headers = default_headers
    try:
        r = requests.get(url, headers=headers, timeout=30)
        if r.status_code == 200:
            try:
                return r.json()
            except:
                return None
        else:
            print("Error response code: " + str(r.status_code))

    except requests.exceptions.HTTPError:
        print("Http error, retry")
    except requests.exceptions.ConnectionError:
        print("Connection error, retry")
        return api_get(url, headers)
    except requests.exceptions.Timeout:
        print("Request timeout, retry")
        time.sleep(1)
        return api_get(url, headers)
    except requests.exceptions.RequestException:
        print("Something else error, retry")


def api_post(url, data, headers=None):
    # if set none, use default headers
    if headers is None:
        headers = default_headers
    try:
        r = requests.post(url, data=json.dumps(data), headers=headers, timeout=30)
        if r.status_code == 200:
            return r.json()
        else:
            print("Error response code: " + str(r.status_code))

    except requests.exceptions.HTTPError:
        print("Http error, retry")
    except requests.exceptions.ConnectionError:
        print("Connection error, retry")
        return api_post(url, data, headers)
    except requests.exceptions.Timeout:
        print("Request timeout, retry")
        time.sleep(1)
        return api_post(url, data, headers)
    except requests.exceptions.RequestException:
        print("Something else error, retry")
