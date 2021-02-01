#  Author Sucsz(Vladimir Semykin)

def traj_num(goal):
    """
    Функция считает количество возможных способов попасть из начальной точки, в заданную точку goal
    Если возможны следующие ходы:
    1) current_position +1
    2) current_position +2
    :param goal: int, Конечная точка
    :return: int, количество возможных сопособов попасть
    """
    dots = [0, 1] + [0] * goal
    for counter in range(2, goal + 1):
        dots[counter] = dots[counter - 2] + dots[counter - 1]
    return dots[goal]


def count_traj(goal, allowed: list):
    """
    Функция считает количество возможных способов попасть из начальной точки, в заданную точку goal
    Если возможны следующие ходы:
    1) current_position +1
    2) current_position +2
    3) current_position +3
    :param goal: int, Конечная точка
    :param allowed: булевский список значений, возможно ли попасть в точку или нет
    :return: int, количество возможных сопособов попасть
    """
    dots = [0, 1, allowed[2]] + [0] * (goal - 3)
    for counter in range(3, goal+1):
        if allowed[counter]:
            dots[counter] = dots[counter - 1] + dots[counter - 2] + dots[counter - 3]
    return dots[goal]


def count_min_cost(goal, price: list):
    """
    Функция считает минимальную стоимость, чтобы попасть из начальной точки, в заданную точку goal
    Если возможны следующие ходы:
    1) current_position +1
    2) current_position +2
    :param goal: int, Конечная точка
    :param price: list, список стоимостей достижения клеток
    :return: int, минимальная стоимость достижения клетки goal
    """
    dots = [None, price[1], price[1] + price[2]] + [0] * (goal - 2)
    for counter in range(3, goal + 1):
        dots[counter] = price[counter] + min(dots[counter - 1], dots[counter - 2])
    return dots[goal]
