#  Author Sucsz(Vladimir Semykin)

def fast_pow(x: float, y: int):
    """
    Функция для быстрого возведения в степень
    :param x: float, число - которое возводим
    :param y: int, число - в которое возводим
    :return: float, x**y
    """
    if y == 0:
        return 1
    elif not(y % 2):
        return fast_pow(x ** 2, y // 2)
    else:
        return pow(x, y-1) * x


print(fast_pow(2, 100))
