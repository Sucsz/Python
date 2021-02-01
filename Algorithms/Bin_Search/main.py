#  Author Sucsz(Vladimir Semykin)

def left_bound(array, key):
    """
    Функция выполняет поиск левой границы(индекса) искомого элемента в массив array, иначе -1
    :param array: list - массив, где осуществляется поиск
    :param key: - искомый элемент
    :return: int - индекс левой границы
    """
    left = -1
    right = len(array)
    while right - left > 1:
        middle = (left + right) // 2
        if array[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(array, key):
    """
    Функция выполняет поиск правой границы(индекса) искомого элемента в массив array, иначе длину массива
    :param array: list - массив, где осуществляется поиск
    :param key: - искомый элемент
    :return: int - индекс правой границы
    """
    left = -1
    right = len(array)
    while right - left > 1:
        middle = (left + right) // 2
        if array[middle] <= key:
            left = middle
        else:
            right = middle
    return right


def bin_search(array: list, key: int):
    """
    Функция выполняет поиск левой и правой границ(индексов) искомого элемента в массив array
    :param array: list - массив, где осуществляется поиск
    :param key: - искомый элемент
    :return: int - индекс правой границы
    """
    left_b = left_bound(array, key)
    right_b = right_bound(array, key)
    if abs(left_b - right_b) <= 1:
        print(f"Элемент {key} не найден")
        return
    print(f"элемент {key} найден, левая граница(индекс) - {left_b}, правая граница(индекс) - {right_b}")
    return {left_b, right_b}


test_array = [1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9]
bounds = bin_search(test_array, 6)
