#  Author Sucsz(Vladimir Semykin)

def sieve_of_eratosthenes(count: int):
    """
    Функция реализует алгоритм "Решето Эратосфера"
    :param count: int, Вывод для первых (count-1) чисел
    :return: void, функция выводит результат на экран
    """
    array = [True] * count
    array[0] = array[1] = False
    for k in range(2, count):
        if array[k]:
            for j in range(2*k, count, k):
                array[j] = False
    for k in range(count):
        print(k, '-', "простое" if array[k] else "составное")


sieve_of_eratosthenes(100)
