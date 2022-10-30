def get_count_char(str_):
    dict = {}
    new_str_ = str_.lower()
    for letter in new_str_:
        if letter.isalpha():
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
    return dict



main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def get_5(data):
    dict_1 = dict()
    sum_ = sum(data.values())
    for k,v in data.items():
        percent = round(v * 100 / sum_,2)
        dict_1[k] = dict_1.get(k, percent)
    return dict_1
print(get_5(get_count_char(main_str)))
