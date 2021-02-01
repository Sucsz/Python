# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:57:03 2020

@author: sucsz
"""

# Модуль cards
# Набор базовых классов для карточной игры
class Card(object):
    """ Одна игральная карта """
    RANKS = [ "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"] # c - clubs(крести)  d - diamonds - бубны(ромбики)
                                 # h - hearts(червы)  s -spades    - пики
    def __init__(self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep
    def flip(self):
        """ Переворот карты """
        self.is_face_up = not self.is_face_up
class Hand(object):
    """ 'Рука': набор карт на руках у одного игрока """
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<пусто>"
        return rep 
    def clear(self):
        """ Очистка карт """
        self.cards = []
    def add(self, card):
        """ Добавить карту """
        self.cards.append(card)
    def give(self, card, other_hand):
        """ Отдать карту """
        self.cards.remove(card)
        other_hand.add(card)
class Deck(Hand):
    """ Колода игральных карт  """
    def populate(self):
        """ Наполнение колоды """
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
    def shuffle(self):
        """ Перемешка колоды """
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand = 1):
        """ Раздача карт на руки с выбранным количеством, по умолчанию 1 """
        for rounds in range(per_hand):
            if len(self.cards)<1:
                self.clear()
                self.populate()
                self.shuffle()
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Не могу больше сдавать, карты закончились!")
                    
if __name__ == "__main__":
    print("Это модуль содержащий классы для карточных игр")
    input("\n\nНажмите Enter, чтобы выйти")