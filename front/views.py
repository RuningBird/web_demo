from django.shortcuts import render
from django.http.response import JsonResponse
from front import fun_tools, fun_mongo
import json


# Create your views here.

def index(request):
    return render(request, 'html/index.html')


def distribution_capacity(request):
    r = fun_tools.get_capacity_distribution()
    context = {
        'distribution_capacity': r
    }

    return render(request, 'html/capacity_distribution.html')


def capacity_grow(request):
    context = fun_tools.get_capacity_grow()

    return render(request, 'html/grow_vertical.html', context=context)


def person_work_ship_info(request):
    context = fun_tools.get_persion_work_ship_info()

    return render(request, 'html/person_work_ship_list.html', context=context)


def distribution_ship_person_number(request):
    context = fun_tools.get_ships_person_number()
    return render(request, 'html/ship_person_number.html', context)


def person_details(request):
    context = {
        'segments': ['a', 'b'],
        'array_values': [[1, 2], [3, 4]]
    }

    # context = fun_tools.get_person_details()
    context = fun_mongo.get_person_details()  # 替换为mongodb
    return render(request, 'html/persion_details.html', context)


# In[1] 值请求类
##############################
def json_capacity_distribution(request):
    r = fun_tools.get_capacity_distribution()
    context = {
        'distribution_capacity': r
    }

    return JsonResponse(context)


def json_persion_work_ship_info(request):
    context = fun_tools.get_persion_work_ship_info()
    context = {
        'data': [
            {
                'children': [
                    {
                        'children': [],
                        'name': 'a'
                    }
                ],
                'name': 'David Williams'
            }
        ]
    }
    return JsonResponse(context)
