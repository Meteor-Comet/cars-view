# Create your views here.
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import getPublicData, getCenterData
from .utils import getCenterLeftData
from .utils import getBottomLeftData
from .utils import getCenterRightData
from .utils import getCenterChangeData
from .utils import getBottomRightData


def center(request):
    if request.method == 'GET':
        sumCar, highVolume, topCar, mostModel, mostBrand, averagePrice = getCenterData.getBaseData()
        lastSortList = getCenterData.getRollData()
        oilRate, electricRate, mixRate = getCenterData.getTypeRate()
        return JsonResponse({
            'sumCar': sumCar,
            'highVolume': highVolume,
            'topCar': topCar,
            'mostModel': mostModel,
            'mostBrand': mostBrand,
            'averagePrice': averagePrice,
            'lastSortList': lastSortList,
            'oilRate': oilRate,
            'electricRate': electricRate,
            'mixRate': mixRate
        })


def centerLeft(request):
    if request.method == 'GET':
        lastPieList = getCenterLeftData.getPieBrandData()
        return JsonResponse({
            'lastPieList': lastPieList
        })


def bottomLeft(request):
    if request.method == 'GET':
        brandList, volumeList, priceList = getBottomLeftData.getSquareData()
        return JsonResponse({
            'brandList': brandList,
            'volumeList': volumeList,
            'priceList': priceList
        })


def centerRight(request):
    if request.method == 'GET':
        realData = getCenterRightData.getPriceSortData()
        return JsonResponse({
            'realData': realData
        })


def centerRightChange(request, energyType):
    if request.method == 'GET':
        oilData, electricData = getCenterChangeData.getCircleData()
        realData = []
        if energyType == 1:
            realData = oilData
        else:
            realData = electricData
        return JsonResponse({
            'realData': realData
        })


def bottomRight(request):
    if request.method == 'GET':
        carData = getBottomRightData.getRankData()
        return JsonResponse({
            'carData': carData
        })


