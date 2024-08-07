import json
import time
from .getPublicData import *

def getBaseData():
    cars = list(getAllCars())
    sumCar = len(cars)
    highVolume = cars[0].saleVolume
    topCar = cars[0].carName
    #车型
    carModels = {}
    maxModel = 0
    mostModel = ''
    for i in cars:
        if carModels.get(i.carModel,-1) == -1:
            carModels[str(i.carModel)] =1
        else:
            carModels[i.carModel] += 1
    carModels = sorted(carModels.items(),key=lambda x:x[1],reverse=True)
    mostModel = carModels[0][0]
    #品牌
    carBrand = {}
    maxBrand = 0
    mostBrand = ''
    for i in cars:
        if carBrand.get(i.brand,-1) == -1:
            carBrand[str(i.brand)] =1
        else:
            carBrand[str(i.brand)] += 1
    for k,v in carBrand.items():
        if v > maxBrand:
            maxBrand = v
            mostBrand = k
    #价格
    carPrices = {}
    averagePrice = 0
    sumPrice = 0
    for i in cars:
        x = json.loads(i.price)[0] + json.loads(i.price)[1]
        sumPrice += x
    averagePrice = sumPrice / (sumCar * 2)
    averagePrice = round(averagePrice, 2)
    return sumCar,highVolume,topCar,mostModel,mostBrand,averagePrice

def getRollData():
    cars = list(getAllCars())
    #品牌
    carBrand = {}
    for i in cars:
        if carBrand.get(i.brand,-1) == -1:
            carBrand[str(i.brand)] =1
        else:
            carBrand[str(i.brand)] += 1
    brandlist = [(value,key) for key,value in carBrand.items()]
    brandlist = sorted(brandlist,reverse=True)[0:10]
    sortDict = {i[1]:i[0] for i in brandlist}
    lastSortList= []
    for k,v in sortDict.items():
        lastSortList.append(
            {
                'name':k,
                'value':v
            }
        )
    return lastSortList

def getTypeRate():
    cars = list(getAllCars())
    #能源类型
    carTypes = {}
    counts = len(cars)
    for i in cars:
        if carTypes.get(i.energyType,-1) == -1:
            carTypes[str(i.energyType)] =1
        else:
            carTypes[str(i.energyType)] += 1
    oilRate = round(((carTypes['汽油']+ carTypes['油电混合']+ carTypes['48V轻混系统']) / counts)*100,2)
    mixRate = round(((carTypes['插电式混合动力']+ carTypes['增程式']) / counts)*100,2)
    electricRate = round((carTypes['纯电动'] / counts)*100,2)
    return oilRate,electricRate,mixRate