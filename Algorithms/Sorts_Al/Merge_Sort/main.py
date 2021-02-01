#  Author Sucsz(Vladimir Semykin)

def merge_sort(array: list):
    """
    Функция реализует сортировку слиянием, сортируя входящий массив и возвращая новый массив
    :param array: list, сортируемый массив
    :return: list, sorted array
    """
    if len(array) < 2:
        return array[:]
    middle = len(array) // 2
    #  left = merge_sort(array[:middle])
    #  right = merge_sort(array[middle:])
    return merge(merge_sort(array[:middle]), merge_sort(array[middle:]))


def merge(left, right):
    """
    Вспомогательная функция для слияния левой и правой части в единое целое
    :param left: list
    :param right: list
    :return: list - sorted array
    """
    result = []
    l, r = 0, 0  # l - индекс для левой части, r - для правой
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            result.append(right[r])
            r += 1
        else:
            result.append(left[l])
            l += 1
    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1
    return result


print(merge_sort([1, 2, 3, 100, 77, 144, 10, 15, 15, 3]))
