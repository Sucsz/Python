#  Author Sucsz(Vladimir Semykin)

def factorize_number(number):
    """
    Раскаладывает число на множители
    :param number: int - число, которое требуется разложить, диапозон от 2 до верхней границы int
    :return: divisors: list - список множителей числа
    """
    divisors = []
    divisor = 2
    while number > 1:
        if not (number % divisor):
            divisors.append(divisor)
            number //= divisor
        else:
            divisor += 1
    return divisors


divs = factorize_number()
print(*divs)
