def single_root_words(root_word, *other_words):
    same_words = []
    for perem in other_words:  # перебор списка other_word  с названием каждого элемента по очереди названным perem
        if root_word.lower() in perem.lower() or perem.lower() in root_word.lower(): # если root_word есть в perem, lower() - переводим в нижний регистр
            same_words.append(perem)   #добавили найденое слово в список
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagle')
print(result1)
print(result2)