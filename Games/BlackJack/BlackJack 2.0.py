# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 20:50:28 2020

@author: sucsz
"""
# Блек-джек
# От 1 до 7 игроков против диллера
import cards, player_in_game
class BJ_Card(cards.Card):
    """ Карта для игры в Black-Jeck """
    ACE_VALUE = 1
    @property
    def value(self):
        """ Номинал карты """
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v
class BJ_Deck(cards.Deck):
    """ Колода для игры в Black-Jeck """
    def populate(self):
        """ наполнение колоды"""
        self.cards = []
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))
class BJ_Hand(cards.Hand):
    """ 'Рука': набор карт 'Black-Jeck' у одного игрока """
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name
    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep
    @property
    def total(self):
        """ Возвращает количество очков в руке """
        # Если у одной из карт value равно None, то и все свойство None
        for card in self.cards:
            if not card.value:
                return None
        # Суммируем очки, считая туз за 1 очко
            t = 0
        for card in self.cards:
            t += card.value
         # Определяем, есть ли туз на руках у игрока
            contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
        # Если есть на руках туз и сумма очков не привышает 11, будем 
        # считать туз за 11 очков
        if contains_ace and t <= 11:
        # Прибавим 10, так как туз уже посчитан за 1
            t += 10
        return t
    def is_busted(self):
        """ Проверка на то, чтобы количество очков было меньше 21 """
        return self.total > 21
class BJ_Player(BJ_Hand):
    """ Игрок в Black-Jeck """
    def is_getting(self):
        """ Вопрос о доборе карт для игрока """
        response = player_in_game.ask_yes_no("\n" + self.name + 
        ", будете брать еще карты? (y/n): "
                                    )
        return response == "y"
    def bust(self):
        """ Перебор """
        print(self.name, "перебрал")
        self.lose()
    def lose(self):
        """ Проигрыш """
        print(self.name, "проиграл")
    def win(self):
        """ Выигрыш """
        print(self.name, "выиграл")
    def draw(self):
        """ Ничья """
        print(self.name, "сыграл с компьютером вничью")
class BJ_Dealer(BJ_Hand):
    """ Дилер в игре Black-Jeck """
    def is_getting(self):
        """ Проверка для добора карт """
        return self.total < 17
    def bust(self):
        """ Перебор """
        print(self.name, "перебрал")
    def flip_first_card(self):
        """ Переворачивает первую карту диллера лицевой стороной вниз """
        firs_card = self.cards[0]
        firs_card.flip()
class BJ_Game(object):
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
        self.dealer = BJ_Dealer("Dealer")
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
    @property
    def still_playing(self):
        """ Составляет список невылетевших игроков """
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp
    def __additional_cards(self, player):
        """ Добор карт + проверка наличия карт в колоде """
        while not player.is_busted() and player.is_getting():
            if len(self.deck.cards)<1:
                self.deck.clear()
                self.deck.populate()
                self.deck.shuffle()
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
    def play(self):
        """ Основной цикл игры """
    # Сдача всем по 2 карты
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card() #первая из карт, сданных диллеру 
                                  #переворачивается рубашкой вверх
        for player in self.players:
            print(player)
        print(self.dealer)
    # Cдача дополнительных карт игрокам
        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card() #первая карта диллера раскрывается
        if not self.still_playing:
    # Все игроки перебрали, покажем только руку дилера
            print(self.dealer)
        else:
    # Сдача доплнительных карт дилеру
            print(self.dealer)
            self.__additional_cards(self.dealer)
            if self.dealer.is_busted():
        # Выигрывают все оставшиеся игроки
                for player in self.still_playing:
                    player.win()
            else:
        # Сравниваем суммы очков у диллера и игроков оставшихся в игре
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.draw()
    # Удаление всех карт
        for player in self.players:
            player.clear()
        self.dealer.clear()
def main():
    """ Основная часть программы """
    print("\tДобро пожаловать в игру Black-Jack")
    names = []
    number = player_in_game.ask_number("Сколько игроков учавствует ? (1-7): ",
                                       1,
                                       7
                                       )
    # Передаем имена
    for i in range(number):
        name = input("Введите имя игрока:")
        names.append(name)
        print()
    game = BJ_Game(names)
    again = None
    while again != "n":
        game.play()
        again = player_in_game.ask_yes_no("\nХотите сыграть еще раз ? (y/n): ")
main()
input("нажмите enter, чтобы выйти")