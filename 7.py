def sum_of_digits(number):
    result = sum([int(x) for x in str(number)])
    return result


print(sum_of_digits(1321423))