calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    s = (len(string), string.upper(), string.lower())
    count_calls()
    return s


def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [s.lower() for s in list_to_search]


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
