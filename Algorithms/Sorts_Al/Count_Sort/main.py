def count_sort(array: list):
    """
    Сортирует список натуральных чисел, где количество различных чисел сравнительно мало
    :param array: list - сортируемый список
    :return: void - сортирует список, переданный в функцию
    """
    scope = max(array) + 1  # Для натуральный чисел это наилучший вариант
    print(scope)
    freq_array = [0] * scope
    for x in array:
        freq_array[x] += 1
    array[:] = []
    for number in range(scope):
        array += [number] * freq_array[number]
        print(array)


array1 = [x for x in range(11)] + [x for x in range(11)] + [3]
count_sort(array1)
