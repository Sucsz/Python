#  Author Sucsz(Vladimir Semykin)

def prefix_function(str):
    """
    Префикс-функция возвращающая массив длин префиксов=суффиксам
    :param str: строка для поиска
    :return: list
    """
    pi = [0 for i in range(len(str))]
    for counter in range(1, len(str)):
        p = pi[counter - 1]
        while p > 0 and str[counter] != str[p]:
            p = pi[p - 1]
        if str[counter] == str[p]:
            p += 1
        pi[counter] = p
    return pi


def kmp(haystack, needle):
    """
    Функция, реализующая алгоритм Кнута-Морриса-Пратта
    :param haystack: str - строка для поиска
    :param needle: str - подпоследовательность, которую ищем
    :return:
    """
    index = -1
    pi = prefix_function(needle)
    k = 0
    for i in range(len(haystack)):
        while k > 0 and needle[k] != haystack[i]:
            k = pi[k - 1]
        if needle[k] == haystack[i]:
            k += 1
        if k == len(needle):
            index = i - len(needle) + 1
            return index
    print("Вхождение образца в строку не обнаружено")
    return index


print(max(prefix_function("abafaba")))
print(kmp("Абракадабра", "кадабр"))
