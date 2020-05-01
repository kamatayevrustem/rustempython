import json
from pprint import pprint

def topstring(name_of_file):
    list = []
    sort_list = []
    top = []
    file = name_of_file
    #читаем файл
    with open(file, 'r', encoding='utf-8') as myfile:
        data=json.load(myfile)

    for news in data:
       for new in data[news]:
           if new=='channel':
               for description in data[news][new]:
                   if description == 'items':
                       for descriptions in data[news][new]['items']:
                           list.append(descriptions)
    for item in list:
        all = item['description']
    sort_list = all.split(' ')

    #функция сортировки
    def myFunc(e):
      return len(e)
    sort_list.sort(key=myFunc,reverse=True)

    # больше 6ти символов
    for key in sort_list:
        if len(key)>6:
            top.append(key)
    print(top[0:6])



topstring('file.json')
topstring('file2.json')




