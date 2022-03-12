# @author: Guido Enrique
# @github: /guidoenr
# @gitlab: /guidoenr

import requests
import logger
import json

COINGECKO_API = 'https://api.coingecko.com/api/v3'

"""
payload = {
    'deveoper_data': 'true', 
    'market_data': 'true',
    'page': 1
}
"""
def get_data(subdomain:str, *params): # params could be optional
    url = COINGECKO_API + subdomain
    return requests.get(url, *params).json() # it is str

if __name__ == '__main__':
    #print(get_request("/ping"))
    #print(get_request("/coins/list"))
    #print(get_request("/coins/categories/list"))
    data = get_data("/coins/bitcoin/")
    
    