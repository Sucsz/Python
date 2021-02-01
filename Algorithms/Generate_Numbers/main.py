#  Author Sucsz(Vladimir Semykin)

def generate_numbers(base: int, length: int, prefix=None):
    """
    Генерирует все числа (с лидирующими незначищими нулями)
    в base-ричной системе счисления (base <= 10)
    длины M
    :param base: int, основание системы счисления
    :param length: int, длина числа
    :param prefix: list, префикс числа
    :return: void, выводит числа на экран
    """
    prefix = prefix or []
    if not (length):
        print(*prefix)
        return
    for digit in range(base):
        prefix.append(digit)
        generate_numbers(base, length - 1, prefix)
        prefix.pop()


def gen_bin(length, prefix=""):
    """
    Генерирует все двоичные числа заданной длины
    :param length: int - заданная длина
    :param prefix: list
    :return: void, выводит числа на экран
    """
    if not (length):
        print(prefix)
        return
    for digit in '0', '1':
        gen_bin(length-1, prefix+digit)
    #  gen_bin(length - 1, prefix + '0')
    #  gen_bin(length - 1, prefix + '1')


generate_numbers(10, 3)
gen_bin(4)
