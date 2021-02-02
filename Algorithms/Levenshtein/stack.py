#  Author Sucsz(Vladimir Semykin)

def levenshtein(array1, array2):
    """
    Функция вычисляет редакционное расстояние Левенштейна
    :param array1: str - строка для сравнения
    :param array2: str - строка для сравнения
    :return: int - редакционное расстояние Левенштейна
    """
    distances = [[(counter1+counter2) if counter1*counter2 == 0 else 0 for counter2 in range(len(array2) + 1)]
                 for counter1 in range(len(array1)+1)]
    for counter1 in range(1, len(array1) + 1):
        for counter2 in range(1, len(array2) + 1):
            if array1[counter1-1] == array2[counter2-1]:
                distances[counter1][counter2] = distances[counter1-1][counter2-1]
            else:
                distances[counter1][counter2] = 1 + min(distances[counter1 - 1][counter2],
                                                        distances[counter1][counter2-1],
                                                        distances[counter1-1][counter2-1])
    return distances[len(array1)][len(array2)]


print(levenshtein("abcd", "efgh"))
