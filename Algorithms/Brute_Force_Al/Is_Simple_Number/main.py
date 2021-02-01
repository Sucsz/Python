#  Author Sucsz(Vladimir Semykin)

def is_simple_number(number):
    """
    Определяет является ли число простым
    :param number: int - число, которое требует проверки, число лежит в диапозооне от 3 до верхней границы int
    :return: bool, возвращает логическое значение типа bool, True - число простое, False - составное.
    >>> is_simple_number(5)
    True
    >>> is_simple_number(10)
    False
    """
    divisor = 2
    while divisor < number:
        if not (number % divisor):
            return False
        divisor += 1
        return True


for counter in range(3, 100):
    print(f"{counter} - {is_simple_number(counter)}")

