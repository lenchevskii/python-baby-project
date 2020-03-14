# real function
def real_numbers_generator(minimum, maximum, step):
    return list(range(minimum, maximum, step))


# memory safe factorial (this recursion makes me happy, because it call only one stack frame)
# 'tce' is a tail call eliminated function (save recursion trick)
def factorial(number):
    def tce_factorial(num):
        if num == 0:
            return 1
        elif num < 0:
            return "It's impossible to get factorial of negative number."
        else:
            return num * tce_factorial(num - 1)

    return tce_factorial(number)


def comparison(list_of_numbers, comparison_number):
    return list(filter(lambda x: x > comparison_number, list_of_numbers))


# unique character only
def accumulator_function(txt):
    median = list(map(lambda x: x.lower(), list(txt)))
    return "-".join(list(map(lambda y: (y + y * median.index(y)).capitalize(), median)))


def check_greeting(string):
    import re
    greetings = '\\b|\\b'.join(['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc'])
    pattern = f'(?i)\\b{greetings}\\b'
    return re.findall(pattern, string)


# points_of_team helper
def comparator(xy):
    [x, y] = xy
    if x > y:
        return 3
    elif x == y:
        return 1
    else:
        return 0


# cross lambda method
def points_of_team(matches):
    return list(map(lambda xy: comparator(xy),
                    list(map(lambda res: list(map(lambda parse: int(parse),
                                                  res.split(':'))), matches))))


if __name__ == "__main__":
    print(real_numbers_generator(10, 20, 1))
    print(factorial(10))
    print(comparison(list(range(-10, 20)), 5))
    print(accumulator_function('AvTj'))
    print(check_greeting('Hello I am Dima and this not a joke, just salut ccciao'))
    print(points_of_team(['3:4', '1:0', '3:3']))
