#  Author Sucsz(Vladimir Semykin)

def cyclic_left_shift(array: list, count: int):
    """
    Функция осуществляет циклический сдвиг массива влево на указанное число позиций count
    :param array: list
    :param count: int
    :return: void, изменяет массив, который был передан в функцию
    """
    tmp = array[0]
    for k in range(count - 1):
        array[k] = array[k + 1]
    array[count - 1] = tmp


def cyclic_right_shift(array: list, count: int):
    """
    Функция осуществляет циклический сдвиг массива вправо на указанное число позиций count
    :param array: list
    :param count: int
    :return: void, изменяет массив, который был передан в функцию
    """
    tmp = array[count - 1]
    for k in range(count - 2, -1, -1):
        array[k + 1] = array[k]
    array[0] = tmp


def test_cyclic_left_shift():
    array1 = [0, 1, 2, 3, 4]
    cyclic_left_shift(array1, 5)
    if array1 == [1, 2, 3, 4, 0]:
        print("test1 - ok")
    else:
        print("test1 - false")


def test_cyclic_right_shift():
    array1 = [0, 1, 2, 3, 4]
    cyclic_right_shift(array1, 5)
    if array1 == [4, 0, 1, 2, 3]:
        print("test2 - ok")
    else:
        print("test2 - false")


test_cyclic_left_shift()
test_cyclic_right_shift()
