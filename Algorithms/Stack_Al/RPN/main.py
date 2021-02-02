#  Author Sucsz(Vladimir Semykin)

import stack

OPERATORS = {
    '+': float.__add__,
    '-': float.__sub__,
    '*': float.__mul__,
    '^': float.__pow__,
}


def reverse_polish_notation(rpn: list):
    """
    Функция вычисляет выражение записанное в обратной польской нотации
    :param rpn: str - выражение, записанное в польской нотации
    :return: float - результат выражения
    """
    for token in rpn:
        if token not in OPERATORS:
            stack.push(token)
        else:
            y = float(stack.pop())
            x = float(stack.pop())
            z = OPERATORS[token](x, y)
            stack.push(z)
    return stack.pop()


print(reverse_polish_notation([5, 3, '+', 4, '*']))
