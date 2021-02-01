# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 00:00:22 2019

@author: sucsz
"""

#Крестики-нолики
#Компьютер против пользователя


#Глобальные константы
X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9
def display_instruct():
    """Выводит на экран инструкцию для игрока"""
    print(
            """
            Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времен.
            Твой мозг и мой процессор сойдутся в схавтке за доской игры "Крестики-Нолики".
            Чтобы сделать ход, введи число от 0 до 8. Числа однозначно соответсвуют полям доски - так,
            как показано ниже:
            0 | 1 | 2
            ---------
            3 | 4 | 5
            ---------
            6 | 7 | 8
            Приготовься к бою, кожаный ублюдок. Вот-вот начнется сражение.\n
            """
            )
        
        
def  ask_yes_no(question):
    """Задает вопрос пользователю и просит ответ, `да` или `нет`"""
    answer = None
    while answer not in ("y","n"):
        answer = input(question).lower()
    return(answer)
    
    
def ask_number(question, low, high):
    """Просит ввести число из диапозона квадратов"""
    answer = None
    while answer not in range(low, high):
        answer = int(input(question))
    return answer


def chips():
    """Определяет принадлежность первого хода"""
    go_first = ask_yes_no("Хочешь оставить за собой право первого хода? (y/n): ")
    if go_first == "y":
        print("\nНу что ж, я даю тебе фору, играй крестиками.")
        human = X
        computer = O
    else:
        print("\n Твоя удаль тебя погубит... Буду начинать я")
        computer = X
        human = O
    return computer, human


def new_board():
    """Создает новую игровую доску"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Отображает доску на экране"""
    print("\n\t",board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")
    
    
def legal_moves(board):
    """Создает список доступных ходов"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Определяет победителя в игре"""
    WAYS_TO_WIN = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (0,4,8),
                   (2,4,6)
                   )
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None
def human_move(board, human):
    """Получает ход человека"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из полей (0-8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nСмешной кожаный кусок дерьма! Это поле уже занято, выбери дургое\n")
    print("Ладно..")
    return move


def computer_move(board, computer, human):
    """Делает ход за копмьюетрного противника"""
    #Создадим рабочую копию доски, потому что функция будет меня некоторые
    #значения в списке
    board = board[:]
    """
    Стратегия: 
        1) Если существует такой ход компьютера, после которого он может выиграть,
        то нужно сделать этот ход
        2) Если существует такой ход человека, после которого он одерживает победу на
        следующем ходу, нужно его предупредить
        3) В ином случае компьютер выбирает для своего хода "лучшее" из доступных полей
        Будем считать, что лучшее поле - центральное, ему устпуают угловые, а тем
        все остальные
        создадим кортеж "лучших полей", чтобы раздать приоритеты, так как в кортеже
        важен порядок
        """
#Поля от лучшего к худшему
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер", end="")
    for move in legal_moves(board):
        board[move] = computer
#Если можно победить выберем этот ход
        if winner(board) == computer:
            print(move)
            return move
#Выполнив проверку, отменим все изменения
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
#Если на следующем ходу выигрывает человек, нужно это прудпредить
        if winner(board) == human:
            print(move)
            return(move)
# Выполнив проверку, отменим все изменения
        board[move] = EMPTY
# Так как нет победы ни у кого этим или следующим ходом то компьютер делает "лучший ход"
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
        
        
def next_turn(turn):
    """Осуществляет переход хода"""
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    """Поздравляет победителя игры"""
    if the_winner != TIE:
        print("три", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Всё как я и предсказывал, ты проиграл тупой кожаный ублюдок")
    elif the_winner == human:
        print("невозможно! Неужели тупой кожаный мешок смог перехетрить меня")
    elif the_winner == TIE:
        print("Тебе несказанно повезло, кожаный мешок дерьма, ты сумел свести игру вничью")
        
        
def main():
    display_instruct()
    computer, human = chips()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


#Запуск программы
main()
input("Нажмите Enter, чтобы выйти")