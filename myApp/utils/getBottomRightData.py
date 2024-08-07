import json
import time
from .getPublicData import *

def getRankData():
    cars = list(getAllCars())
    carData = []
    for car in cars:
        car.price = car.price.replace('[','')
        car.price = car.price.replace(']','')
        car.price = car.price.replace(', ','-')
        carData.append({
            'brand':car.brand,
            'rank':car.rank,
            'carName':car.carName,
            'carImg':car.carImg,
            'manufacturer':car.manufacturer,
            'carModel':car.carModel,
            'price':car.price,
            'saleVolume':car.saleVolume,
            'marketTime':car.marketTime,
            'insure':car.insure
        })
    return carData