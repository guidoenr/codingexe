#@author:guidoenr
# AttackIQ coding excercise, in hackerrank.com

import requests
import json

def map_food_list(food_list, highest):
    mapped = []
    for el in food_list:
        if el["user_rating"]["average_rating"] == highest:
            mapped.append(el['name'])
    return list(dict.fromkeys(mapped))

def getTopRatedFoodOutlets(city):
    uri = "https://jsonmock.hackerrank.com/api/food_outlets?city={}".format(city)
    total_pages = requests.get(uri).json()["total_pages"]
    food_outlets = []    
    for i in range(1, total_pages+1):
        data = requests.get(uri + "&page={}".format(i)).json()["data"]
        for food in data:
            food_outlets.append(food)
    food_outlets.sort(key=lambda k: k["user_rating"]["average_rating"], reverse=True)
    highest = max(food_outlets, key=lambda ev:ev["user_rating"]["average_rating"])
    mapped = map_food_list(food_outlets, highest["user_rating"]["average_rating"])
    return mapped[:5]
        

if __name__ == '__main__':   
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

#    city = input()

    result = getTopRatedFoodOutlets("Seattle")
    print(result)
#    fptr.write('\n'.join(result))
#    fptr.write('\n')

#    fptr.close()


    


