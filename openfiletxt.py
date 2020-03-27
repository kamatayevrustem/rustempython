from collections import Counter

cook_book = {}
cook_book_foods = []
item = 0
i = 0

def get_shop_list_by_dishes(dishname, count, dict):
    dishes = dishname
    person_count = count
    cooking = dict
    cooking_list = []
    cooking_list_format = {}
    array = []
    temp_quantity = 0

    if person_count > 0:
        # print('У вас сегодня будет', person_count, 'гостя')

        #объединяем продукты в единый список cooking_list
        for cook in cooking:
            for dish in dishes:
                if cook == dish:
                    cooking_list.append(cooking[cook])

        #увеличиваем количество блюд
        for ingredient in cooking_list:
            for foods in ingredient:
                for food in foods:
                    if food == 'quantity':
                        foods[food] = foods[food] * person_count

        # убираем дубли
        for ingredient in cooking_list:
            for item in ingredient:
                namefood = item['ingredient_name']
                measure = item['measure']
                quantity = item['quantity']
                array.append(namefood)
        c = Counter(array)
        for aa in c:
            # print('59', aa, c[aa])
            for ingredient in cooking_list:
                for item in ingredient:
                    namefood = item['ingredient_name']
                    measure = item['measure']
                    quantity = item['quantity']
                    # print('rustem', aa, namefood)
                    if aa == namefood and int(c[aa]) <= 1:
                        # print('без повтора', aa, namefood, quantity)
                        cooking_list_format[namefood] = {'measure': f'{measure}', 'quantity': f'{quantity}'}
                        # print('123')
                    elif aa == namefood and int(c[aa]) > 1:
                        if aa not in cooking_list_format:
                            # print('с повтором', aa, namefood, quantity)
                            temp_quantity = temp_quantity + quantity
                            cooking_list_format[namefood] = {'measure': f'{measure}', 'quantity': f'{quantity}'}
                        elif aa in cooking_list_format:
                            temp_quantity = temp_quantity + quantity
                            cooking_list_format[namefood] = {'measure': f'{measure}', 'quantity': f'{temp_quantity}'}

        print(cooking_list_format)


    else:
        print('\nУ вас сегодня не будет гостей, можете не готовить и посмотреть телевизор')

with open('ingredients_list.txt', 'r', encoding="utf8") as f:
    while i < 4:
        name = f.readline().strip()
        count = int(f.readline().strip())
        # print(name,count)
        while item < count:
            dish = f.readline().strip()
            lst = dish.split(" | ")
            cook_book_foods.append({f'ingredient_name':lst[0], f'quantity':int(lst[1]), f'measure':lst[2]})
            # print('dish:', dish)
            item += 1
        empty = f.readline().strip()
        cook_book[name] = cook_book_foods
        i += 1
        cook_book_foods = []
        item = 0

# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2, cook_book)
