#  Author Sucsz(Vladimir Semykin)

def generate_permutations(numbers: int, pos: int = -1, prefix=None):
    """
    Генерация всех перестановок чисел в диапозоне от 1 до numbers в позициях = pos
    Если параметр pos не передан, то  в позициях = numbers
    :param numbers: int,
    :param pos: int
    :param prefix: list
    :return:
    """
    pos = numbers if pos == -1 else pos  # по умолчанию N чисел в M позициях
    prefix = prefix or []
    if not (pos):
        print(prefix)
        return
    for number in range(1, numbers + 1):
        if number in prefix:
            continue
        prefix.append(number)
        generate_permutations(numbers, pos - 1, prefix)
        prefix.pop()


generate_permutations(10, 3)
