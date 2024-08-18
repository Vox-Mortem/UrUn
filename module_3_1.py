calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(self):
    a = len(self), self.upper(), self.lower()
    count_calls()
    return a


def is_contains(string, list_to_search):
    if string.lower() in [word.lower() for word in list_to_search]:
        count_calls()
        return True
    else:
        count_calls()
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
