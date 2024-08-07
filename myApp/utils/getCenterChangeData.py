import json
import time
from .getPublicData import *


def getCircleData():
    cars = list(getAllCars())
    oilData = []
    eletcricData = []
    for i in cars:
        if i.energyType in ['汽油', '油电混合', '48V轻混系统']:
            oilData.append([i.carName,i.saleVolume,i.energyType])
        elif i.energyType == '纯电动':
            eletcricData.append([i.carName,i.saleVolume,i.energyType])
    oilData = oilData[:10]
    eletcricData = eletcricData[:10]
    return oilData,eletcricData
