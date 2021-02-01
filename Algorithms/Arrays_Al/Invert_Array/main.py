#  Author Sucsz(Vladimir Semykin)

def invert_array(array: list, count: int):
    """
    Обращение массива(поворот задом наперед)
    в рамках игдексов от 0 до count - 1
    :param array: list
    :param count: int
    :return: void, переворачивает массив, переданный в функцию
    """
    for k in range(count // 2):
        array[k], array[count - 1 - k] = array[count - 1 - k], array[k]


def test_invert_array():
    array1 = [1, 2, 3, 4, 5]
    invert_array(array1, 5)
    if array1 == [5, 4, 3, 2, 1]:
        print("test1 - ok")
    else:
        print("test1 - fail")
    array2 = [10, 20, 10, 10, 20]
    invert_array(array2, 5)
    if array2 == [20, 10, 10, 20, 10]:
        print("test2 - ok")
    else:
        print("test2 - fail")


test_invert_array()
