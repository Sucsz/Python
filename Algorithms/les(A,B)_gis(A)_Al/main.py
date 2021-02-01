#  Author Sucsz(Vladimir Semykin)

def les(array1, array2):
    """
    Функция для поиска длины наибольшей общей подпоследовательности
    :param array1: первый массив
    :param array2: второй массив
    :return: int - длина наибольшей общей подпоследовательности
    """
    len_les = [[0] * (len(array2) + 1) for counter in range(len(array1) + 1)]  # + 1 для барьерных полей
    for counter in range(1, len(array1) + 1):
        for counter2 in range(1, len(array2) + 1):
            if array1[counter - 1] == array2[counter2 - 1]:
                len_les[counter][counter] = 1 + len_les[counter - 1][counter2 - 1]
            else:
                len_les[counter][counter2] = max(len_les[counter - 1][counter2], len_les[counter][counter2 - 1])
    return len_les[-1][-1]


print(les([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 7]))


def gis(array):
    """
    Функция для поиска длины наибольшей возрастающей подпоследовательности
    :param array: массив, для поискка
    :return: int - длина наибольшей возрастающей подпоследовательности
    """
    len_gis = [0] * (len(array) + 1)
    for counter in range(1, len(array) + 1):
        m = 0  # максимум
        for counter2 in range(0, counter):
            if array[counter - 1] > array[counter2 - 1] and len_gis[counter2] > m:
                m = len_gis[counter2]
        len_gis[counter] = m + 1
    return len_gis[len(array)]


print(gis([1, 2, 3, 4, 5]))
