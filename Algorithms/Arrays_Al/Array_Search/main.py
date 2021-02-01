#  Author Sucsz(Vladimir Semykin)

def array_search(array: list, count: int, number: int):
    """
    Осуществляет поиск числа number в массиве array от 0 до count-1 включительно
    Возвращает индекс элемента number  массиве array,
    если такие чисел несколько, возвращает индекс первого из них
    или -1, если number не найдено в array
    :param array: list
    :param count: int
    :param number: int
    :return: int
    """
    for ind in range(count):
        if array[ind] == number:
            return ind
    return -1


def test_array_search():
    array1 = [1, 2, 3, 4, 5]
    ind = array_search(array1, 5, 9)
    if ind == -1:
        print("#test1 - ok")
    else:
        print("#test1 - fail")
    array2 = [-1, -2, -3, -4, -5]
    ind = array_search(array2, 5, -3)
    if ind == 2:
        print("#test2 - ok")
    else:
        print("#test2 - fail")
    array3 = [10, 20, 30, 10, 10]
    ind = array_search(array3, 5, 10)
    if ind == 0:
        print("#test3 - ok")
    else:
        print("#test3 - fail")


test_array_search()
