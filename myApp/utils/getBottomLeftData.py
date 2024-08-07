import json
import time
from .getPublicData import *

def getSquareData():
    cars = list(getAllCars())
    carsVolume = {}
    for i in cars:
        if carsVolume.get(i.carName,-1) == -1:
            carsVolume[i.carName] = int(i.saleVolume)
        else:
            carsVolume[i.carName] += int(i.saleVolume)
    carSortVolume = sorted(carsVolume.items(),key=lambda x:x[1],reverse=True)[:15]
    brandList = []
    volumeList = []
    priceList = []
    for i in carSortVolume:
        brandList.append(i[0])
        volumeList.append(i[1])
    for i in cars[:15]:
        priceList.append(float(i.price.replace('[','').split(',')[0]))
    return brandList,volumeList,priceList