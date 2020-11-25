def filter(result):
    for x, y in zip(('FizzBuzz', 'Buzz', 'Fizz'), (15, 5, 3)):
        if result % y == 0:
            return x
    return result


print(list(map(filter, range(1, 101))))