from ast import parse
from turtle import home
from model import *
import api
import model

# TODO, ta feaso
def parse_data(data:dict):
    parsed_data = {
        'name': data['name'],
        'symbol': data['symbol'],
        'homepage': data['links']['homepage'][0],
        'price_change_24h': data['market_data']['price_change_24h'],
        'hashing_algorithm': data['hashing_algorithm']
    }
    return parsed_data

def map_coin(data:dict):
    parsed_data = parse_data(data)
    coin = Coin(**parsed_data)
    session.add(coin)
    session.commit()

def test_map_coins():
    map_coin(api.get_data('/coins/solana'))
    
    map_coin(api.get_data('/coins/bitcoin'))
    
    map_coin(api.get_data('/coins/ethereum'))

    map_coin(api.get_data('/coins/dai'))
    

if __name__ == '__main__':
    
    test_map_coins()
    api.prettify_data(api.get_data('/coins/solana'))
    
