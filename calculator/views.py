from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
'''
def get_shop_list_by_dishes(DATA,key,kol):
    dict = {}
    for key2 in DATA.keys():
        if key == key2:
            dict['recipe'] = DATA[key]
    return dict
'''

def get_shop_list_by_dishes(DATA,key,kol):
    dict = {'recipe' : {}}
    for key2 in DATA.keys():
        if key == key2:
            for key3 in DATA[key2].keys():
                zn = 0
                if key3 not in dict['recipe'].keys():
                    zn = DATA[key2][key3]*kol
                    dict['recipe'][key3] = zn
    return dict


def kolichestvo(request):
    kol = 1
    if request.GET:
        kol = int(request.GET['servings'])
    return kol

def main(request):
    return render(request, 'main.html')

def omlet(request):
    kol = kolichestvo(request)
    context = get_shop_list_by_dishes(DATA,'omlet', kol)
    return render(request, 'calculator/index.html', context)

def pasta(request):
    kol = kolichestvo(request)
    context = get_shop_list_by_dishes(DATA,'pasta')
    return render(request, 'calculator/index.html', context)

def buter(request):
    kol = kolichestvo(request)
    context = get_shop_list_by_dishes(DATA,'buter')
    return render(request, 'calculator/index.html', context)
