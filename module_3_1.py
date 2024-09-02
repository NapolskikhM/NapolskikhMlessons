calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(str_):
    tuple_ = (len(str_), str_.upper(), str_.lower())
    count_calls()
    return tuple_


def is_contains(string, list_to_search):
    string_in_list = False
    for i in list_to_search:
        if i.lower() == string.lower():
            string_in_list = True
            break
    return string_in_list


# Код для проверки
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
