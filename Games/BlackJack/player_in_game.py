# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:35:54 2020

@author: sucsz
"""
# дописать функцию, запршивающую что-то одно
# Игры
# Демонстрирует создание модуля
class Player(object):
    """Участник игры"""
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score
    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep
def ask_yes_no(question):
    """ Задает вопрос с ответом 'y'/'n' """
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response
def ask_number(question, low, high):
    """ Просит ввести число из заданного диапазона """
    try:
        response = None
        while response not in range(low, high + 1):
            response = int(input(question))
        return response
    except ValueError:
        print("Похоже вы ввели не число, попробуйте снова")
        temp_value = ask_number(question, low, high)
        return temp_value
if __name__ == "__main__":
    print("вы запустили этот модуль напрямую, а не импортировали его")
    input("нажмите Enter, чтобы выйти")
        
        