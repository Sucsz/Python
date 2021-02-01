#  Author Sucsz(Vladimir Semykin)

def quick_sort(array):
    """
    Функция реализует быструю сортировку Тони Хоара
    :param array: list, массив для сортировки
    :return: void, реализует быструю сортировку в переданном массиве
    """
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)  # индекс барьерного элемента
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(array, 0, len(array) - 1)


def partition(array, low, high):
    """
    Вспомогательная функция
    Выбираем средний элемент в качестве барьерного
    Также возможен выбор первого, последнего
    или произвольного элементов в качестве барьерного
    :param array: list, массив сортируемых элементов
    :param low: int, левая граница поиска барьерного элемента
    :param high: int, правая граница поиска барьерного элемента
    :return: int, индекс барьерного элемента
    """
    barrier = array[(low + high) // 2]  # Барьерный элемент
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while array[i] < barrier:
            i += 1
        j -= 1
        while array[j] > barrier:
            j -= 1
        if i >= j:
            return j

        # Если элемент с индексом i (слева от барьерного) больше, чем
        # элемент с индексом j (справа от барьерного), меняем их местами
        array[i], array[j] = array[j], array[i]


random_list_of_nums = [22, 5, 1, 1, 4, 100, 18, 99, 100, 1, 18, 99]
quick_sort(random_list_of_nums)
print(random_list_of_nums)
