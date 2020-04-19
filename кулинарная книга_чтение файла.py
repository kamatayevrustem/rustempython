from collections import Counter

def get_shop_list_by_dishes(dishname, count):
    dishes = dishname
    person_count = count
    cooking_list = []
    cooking_list_format = {}
    array = []
    i = 0
    temp_quantity = 0
    a = len(dishes) # количество блюд
    dishes_count = Counter(dishes)
    n = 0
    temp = 0

    # начало программы
    with open('ingredients_list.txt', 'r', encoding="utf8") as f:
        cook_book = {}
        cook_book_foods = []
        item = 0
        i = 0
        while i < 4:
            name = f.readline().strip()
            count = int(f.readline().strip())
            # print(name,count)
            while item < count:
                dish = f.readline().strip()
                lst = dish.split(" | ")
                cook_book_foods.append({f'ingredient_name': lst[0], f'quantity': int(lst[1]), f'measure': lst[2]})
                # print('dish:', dish)
                item += 1
            empty = f.readline().strip()
            cook_book[name] = cook_book_foods
            i += 1
            cook_book_foods = []
            item = 0
    cooking = cook_book


    for cook in dishes_count:
    # cooking_list.append(cook)
        count_food = dishes_count[cook]
        if count_food > 1:
            # print(cook)
            # print(count_food)
            # cooking_list.append(cooking[cook])
            for item in cooking:
                if item == cook:
                    temp = cooking[item]
                    for abs in temp:
                        for inabs in abs:
                            if inabs == 'quantity':
                                abs['quantity']*=count_food*person_count
                        # print(abs)
                    print('')
                    cooking_list.append(temp)
        else:
            # print(cook)
            # print(count_food)
            # cooking_list.append(cooking[cook])
            for item in cooking:
                if item == cook:
                    temp = cooking[item]
                    for abs in temp:
                        for inabs in abs:
                            if inabs == 'quantity':
                                abs['quantity']*=count_food*person_count
                        # print(abs)
                    print('')
                    cooking_list.append(temp)

    # print(cooking_list)


    # форматирую вывод
    for ingredient in cooking_list:
        for item in ingredient:
            namefood = item['ingredient_name']
            measure = item['measure']
            quantity = item['quantity']
            array.append(namefood)
    c = Counter(array)
    # print(c)

    for aa in c:
        # print(c)
        # print(aa)
        # print(c[aa])

        if c[aa] > 1:
            # print(aa)
            print(f'повторяется: {aa}')
            for ingredient in cooking_list:
                for item in ingredient:
                    namefood = item['ingredient_name']
                    measure = item['measure']
                    quantity = int(item['quantity'])
                    if namefood == aa:
                        print(f'{item}, {namefood}')
                        # print(quantity)
                        temp_quantity+=quantity
                        # b = int(quantity)
                        # print(b)
                        # temp+=quantity
                        # cooking_list_format[namefood] = {'measure': f'{measure}', 'quantity': f'{quantity}'}
                    # print(f'{temp}')
                    #     print(temp_quantity)
                        cooking_list_format[namefood] = {'measure': f'{measure}', 'quantity': f'{temp_quantity}'}
            temp_quantity = 0

        else:
            print(f'повторяется: {aa}')
            for ingredient in cooking_list:
                for item in ingredient:
                    namefood = item['ingredient_name']
                    measure = item['measure']
                    quantity = int(item['quantity'])
                    if namefood == aa:
                        # print(namefood)
                        # print(measure)
                        # print(quantity)
                        cooking_list_format[namefood] = {'measure': f'{measure}', 'quantity': f'{quantity}'}

    print(cooking_list_format)


# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
# get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2, cook_book)
# get_shop_list_by_dishes(['Омлет', 'Омлет'], 2, cook_book)
get_shop_list_by_dishes(['Омлет', 'Омлет', 'Омлет', 'Омлет', 'Фахитос', 'Запеченный картофель', 'Запеченный картофель'], 2)
