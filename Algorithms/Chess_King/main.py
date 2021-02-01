#  Author Sucsz(Vladimir Semykin)

def count_traj(height, width):
    """
    Считает количество возможных вариантов добраться в крайнюю точку поля (height, width)
    Для шахматного короля, который может ходить вправо и вниз.
    :param height: int, высота поля
    :param width: int, ширина поля
    :return: количество возможных вариантов добраться в крайнюю точку поля (height, width)
    """
    # Создание сетки(игрвого поля) размером width * height
    # + 1 Используем для создания барьерных полей из 0
    game_board = [[0] * (width + 1) for counter in range(height + 1)]
    game_board[1][1] = 1
    # Чтобы не пересчиать значение клетки (1,1) придеться в ручную посчитать 1-ую линию
    for counter in range(2, width + 1):
        game_board[1][counter] = 1
    for counter in range(2, height+1):  # Обход сверху вниз, слева направо
        for counter2 in range(1, width+1):
            game_board[counter][counter2] = game_board[counter - 1][counter2] + game_board[counter][counter2 - 1]
    return game_board[height][width]


print(count_traj(6, 6))
