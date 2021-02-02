#  Author Sucsz(Vladimir Semykin)

import stack


def check_braces_sequence(string: str):
    """
    Проверяет корректность скобочной последовательности
    :param string: str - строка, в которой проверяется
    :return: bool - True, если скобочная последовательность корректна, иначе False
    >>> check_braces_sequence("((([()])))()([]){}{[]}{([])}")
    True
    >>> check_braces_sequence("(")
    False
    >>> check_braces_sequence("[")
    False
    >>> check_braces_sequence("{")
    False
    >>> check_braces_sequence(")")
    False
    >>> check_braces_sequence("]")
    False
    >>> check_braces_sequence("}")
    False
    >>> check_braces_sequence("[)")
    False
    >>> check_braces_sequence("(]")
    False
    >>> check_braces_sequence("(}")
    False
    >>> check_braces_sequence("{]")
    False
    >>> check_braces_sequence("[(()])")
    False
    """
    for brace in string:
        if brace not in "()[]{}":
            continue
        if brace in "([{":
            stack.push(brace)
        else:
            assert brace in ")]}", "Ожидалась закрываюащя скобка: " + brace
            if stack.is_empty():
                return False
            left = stack.pop()
            assert left in "([{", "Ожидалась открывающая скобка: " + left
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            elif left == "{":
                right = "}"
            if right != brace:
                return False
    return stack.is_empty()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
