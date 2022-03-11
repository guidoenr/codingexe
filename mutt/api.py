# @author: Guido Enrique
# @github: /guidoenr
# @gitlab: /guidoenr

import requests
import logger


COINGECKO_API = 'https://api.coingecko.com/api/v3'

def get_request(subdomain:str, *params):
    url = COINGECKO_API + subdomain
    logger.log(f'GET to {subdomain}, params={params}')
    return requests.get(url, *params).json()

if __name__ == '__main__':
    #print(get_request("/ping"))
    #print(get_request("/coins/list"))
    #print(get_request("/coins/categories/list"))
    payload = {
        'deveoper_data': 'true', 
        'market_data': 'true',
        'page': 1
    }
    get_request("/coins/solana/")