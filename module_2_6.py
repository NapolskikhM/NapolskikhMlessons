# Сначала написал функцию для слов, которые вводит пользователь:
def single_root_words1(root_word = input('Введите слово '), *other_words):
    a = input('Введите несколько слов ')
    a = a.split()
    same_words = []
    for i in range(len(a)):
        if root_word.lower() in a[i].lower(): # Проверка наличия root_word в словах other_words
            same_words.append(a[i])
    for j in range(len(a)):
        if a[j].lower() in root_word.lower(): # Проверка наличия слов other_words в root_word
            same_words.append(a[j])
    return same_words
print('Слова, в которых есть первое слово и наоборот: ', single_root_words1())
print(' ')

# А потом в соответствии с заданием.
def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        a = other_words[i]
        if root_word.lower() in a.lower(): # Проверка наличия root_word в словах other_words
            same_words.append(other_words[i])
    for j in range(len(other_words)):
        a = other_words[j]
        if a.lower() in root_word.lower(): # Проверка наличия слов other_words в root_word
            same_words.append(other_words[j])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
