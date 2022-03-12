from ast import parse
from turtle import home
from model import *
import api
import model


def parse_data(data:dict):
    parsed_data = {
        'name': data['name'],
        'symbol': data['symbol'],
        'homepage': data['links']['homepage'][0],
        'price_change_24h': data['market_data']['price_change_24h']
    }
    return parsed_data

def map_coin(parsed_data:dict):
    print(parsed_data)
    coin = Coin(**parsed_data)
    session.add(coin)
    session.commit()

if __name__ == '__main__':
    data = api.get_data('/coins/solana')
    parsed_data = parse_data(data)
    #api.prettify_data(parse_data(data))
    map_coin(parsed_data)