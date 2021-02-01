def gcd_classic(num1: int, num2: int):
    """
    Функция реализует классический алгоритм Эвклида
    :param num1: int
    :param num2: int
    :return: int
    """
    if num1 == num2:
        return num1
    elif num1 > num2:
        return gcd_classic(num1 - num2, num2)
    else:  # num1 < num2
        return gcd_classic(num2 - num1, num1)


def gcd_modern(num1: int, num2: int):
    """
    Функция реализует усовершенствованный алгоритм Эвклида
    :param num1: int
    :param num2: int
    :return: int
    """
    return num1 if num2 == 0 else gcd_modern(num2, num1 % num2)


print(gcd_classic.__doc__, gcd_classic(100, 40), '\n', gcd_modern.__doc__, gcd_modern(100, 40))
