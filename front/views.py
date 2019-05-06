from django.shortcuts import render
from django.http.response import JsonResponse
from front import fun_tools


# Create your views here.

def index(request):
    return render(request, 'base.html')


def capacity_distribution(request):
    r = fun_tools.get_capacity_distribution()
    context = {
        'capacity_distribution': r
    }

    return render(request, 'html/capacity_distribution.html')


def capacity_grow(request):
    context = fun_tools.get_capacity_grow()

    return render(request, 'html/grow_vertical.html', context=context)


def persion_work_ship_info(request):
    context = fun_tools.get_persion_work_ship_info()

    return render(request, 'html/persion_work_ship_list.html', context=context)


# 值请求类
def json_capacity_distribution(request):
    r = fun_tools.get_capacity_distribution()
    context = {
        'capacity_distribution': r
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
                        'name':'a'
                    }
                ],
                'name': 'David Williams'
            }
        ]
    }
    return JsonResponse(context)
