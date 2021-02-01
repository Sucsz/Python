#  Author Sucsz(Vladimir Semykin)

def insert_sort(array: list):
    """
    Сортировка списка array вставками
    :param array: list - сортируемый список
    :return: void - сортирует массив, переданный в функцию
    """
    for top in range(1, len(array)):
        k = top
        while k > 0 and array[k-1] > array[k]:
            array[k], array[k-1] = array[k-1], array[k]
            k -= 1


def choice_sort(array: list):
    """
    Сортировка списка array выбором
    :param array: list - сортируемый список
    :return: void - сортирует массив, переданный в функцию
    """
    for pos in range(0, len(array)-1):
        for k in range(pos+1, len(array)):
            if array[k] < array[pos]:
                array[k], array[pos] = array[pos], array[k]


def bubble_sort(array: list):
    """
    Сортировка списка array методом пузырька
    :param array: list - сортируемый список
    :return: void - сортирует массив, переданный в функцию
    """
    for bypass in range(1, len(array)):
        for k in range(0, len(array) - bypass):
            if array[k] > array[k+1]:
                array[k], array[k+1] = array[k+1], array[k]


def test_sorted(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    array = list(range(30, -1, -1))
    sort_algorithm(array)
    array_sorted = list(range(31))
    print("Ok\n" if array == array_sorted else "Fail\n")


test_sorted(insert_sort)
test_sorted(choice_sort)
test_sorted(bubble_sort)
