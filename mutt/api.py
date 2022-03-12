# @author: Guido Enrique
# @github: /guidoenr
# @gitlab: /guidoenr
# https://github.com/man-c/pycoingecko TODO

import requests
import logger
import json

COINGECKO_API = 'https://api.coingecko.com/api/v3'

def get_data(subdomain:str, *params): # params could be optional
    url = COINGECKO_API + subdomain
    return requests.get(url, *params).json() # dict

def prettify_data(data:dict):
    print(json.dumps(data, indent=3))


if __name__ == '__main__':
    #print(get_request("/ping"))
    #print(get_request("/coins/list"))
    #print(get_request("/coins/categories/list"))
    data = get_data("/coins/bitcoin/")
    prettify_data(data)
    