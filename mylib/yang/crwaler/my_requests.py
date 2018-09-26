#!usr/bin/env python3

import requests
import os
import logging


def get_content_b(url, **kwargs):
    r = get_response(url, **kwargs)
    if r:
        return r.content
    else:
        return None


def get_content_str(url, **kwargs):
    r = get_response(url, **kwargs)
    if r:
        return r.text
    else:
        return None


def get_response(url, **kwargs):
    try:
        r = requests.get(url, timeout=30, **kwargs)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except Exception as e:
        logging.error(e)
        return None


def get_response_use_mozilla(url, **kwargs):
    kv = {'user-agent': 'Mozilla/5.0'}
    return get_response(url, headers=kv, **kwargs)


def get_response_with_keywords(url, kvs={}, **kwargs):
    return get_response_use_mozilla(url, params=kvs, **kwargs)


def save_img_from_url(url, filename=None, path='.'):
    img_type = url.split(".").pop()
    # can't find a proper type, then let type as jpg
    if len(img_type) > 3:
        img_type = "jpg"
    # if don't give a filename, then let it remain its original name
    if filename is None:
        filename = url.split("/").pop().split(".")[-1]
    filename = filename + "." + img_type
    filename = os.path.join(path, filename)
    with open(filename, 'wb') as f:
        f.write(get_content_b(url))
        f.close()
