import random

dict = {'one':'один', 'two':'два', 'three':'три', 'four':'четыре', 'five':'пять', 'six':'шесть', 'seven':'семь', 'eight':'восемь', 'nine':'девять', 'ten':'десять'}
dict = {'one': 1, 'two':2}
# об'являем функцию
def num_translate(**user_input):
    # если слово - один из ключей
    if user_input in dict.values():
        # вывести соответствующее значение
        print('->', dict[user_input])
        # если слово в значениях словаря
    elif user_input in dict.keys():
        # почти удалось вывести ключ, надо только выяснить, как искать индекс по ключу
        print(list(dict.keys())[list(dict.values()).index(user_input)])
    else:
        print("None")

#index_of_key = [i for i, d in enumerate(dict) if user_input in d.keys()] :

# это хоть и читерское, но решение: вторая функция может искать по двум словарям - один для строчных, один для заглавных
dict_adv = {'One':'Раз', 'Two':'Два', 'Three';'Три', 'Four':'Четыре', 'Five':'Пять', 'Six':'Шесть', 'Seven':'Семь', 'Eight':'Восемь', 'Nine':'Девять', 'Ten':'Десять'}
def num_translate_adv(user_input):
    # если слово начинается с маленькой буквы - делаем то же, что и в первой функции
        if user_input in dict.values():
            print('->', dict[user_input])
        elif user_input in dict.keys():
            print(list(dict.keys())[list(dict.values()).index(user_input)])
            # если с заглавной - ищем во втором словаре
        elif user_input in dict_adv.values():
            print('->', dict_adv[user_input])
        elif user_input in dict_adv.keys():
            print(list(dict_adv.keys())[list(dict_adv.values()).index(user_input)])
        else:
            print("None")

#mylist = input("enter a sentence ")
mylist = ["Иван", "Мария", "Петр", "Илья"]
# делаем функцию для удаления дубликатов из списка
def listsort(lists):
    new_list = []
    for i in lists:
        # если такого еще в списке нет
        if i not in new_list:
            # добавляем в список
            new_list.append(i)
            # и возвращаем список
    return new_list

def thesaurus(mylist):
    # будущий список первых букв
index_list = []
# будущий словарь
dictionary = {}
# для каждой позиции в списке имен
for i in range(0, len(mylist)):
# берем первую букву
    index_list(i) = mylist[i][0]
    # избавляемся от двойных букв
    index_list = listsort(index_list)

# делаем ключи из полученного списка без дубликатов
dictionary.keys() = index_list


# для каждого имени в списке
for word in mylist:
    # для каждого индекса из списка заглавных букв
    for i in range(0, len(index_list):
        # если первая буква совпадает с данным ключом словаря
        if word[0] == dictionary.keys(i)
            dictionary.values(i).append(word) # добавить в словать
# возвращаем словарь | returning the dictionary of first letters and names
return dictionary





def get_jokes(number_of_jokes):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    # import random  подключили пакет рандом в начале и генерим случайный индекс в диапазоне длины листа
    def joker:
        index1 = random.randint(1, len(nouns))
        index2 = random.randint(1, len(adverbs))
        index3 = random.randint(1, len(adjectives))
        joke = [adverbs[index2], nouns[index1], adjectives[index3]]
        return joke
        # выводим набор слов в соответствии со случайными индаксами
        #print(joke[1], joke[2], joke[3])

    # циклим выполнение joker в зависимости от заданного аргумента
    for i in range(1:number_of_jokes)
        print("шутка номер", i, ":", joker())
        
