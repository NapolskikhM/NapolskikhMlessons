def custom_write(file_name, strings):
    dict_ = {}
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(len(strings)):
        dict_[(i + 1, file.tell())] = strings[i]
        file.write(f'{strings[i]}\n')
    file.close()

    return dict_

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

'''((1, 0), 'Text for tell.')
((2, 16), 'Используйте кодировку utf-8.')
((3, 66), 'Because there are 2 languages!')
((4, 98), 'Спасибо!')'''