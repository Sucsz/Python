# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:40:04 2020

@author: sucsz
"""

# Сумашедший сказочник
# Создает рассказ на основе пользовательского ввода
from tkinter import *
class Application(Frame):
    "" "GUI-приложение, создающее рассказ на основе пользовательского ввода """
    def __init__(self, master):
        """ Инициализирует рамку """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """ Создает элементы управления, с помощью которых пользователь будет
    вводить исходные данные и получать готовый рассказ """
    # метка с текстом инструкцией
        Label(self,
              text = "Введите данные для создания нового рассказа"
              ).grid(row = 0, column = 0, columnspan = 3,sticky = W)
    # метка с вводом имени
        Label(self,
              text = "Имя человека:"
              ).grid(row = 1, column =0, sticky = W)
    # метка с вводом существительного во множественном числе
        Label(self,
              text = "Существительное во мн.ч:"
              ).grid(row = 2, column = 0, sticky = W)
    # метка с вводом глагола в инфинитиве
        Label(self,
              text = "Глагол в инфинитиве:"
              ).grid(row = 3, column =0, columnspan = 2,sticky = W)
    # метка для выбора прилагательного(ых)
        Label(self,
              text = "Прилагательное(-ые):",
              ).grid(row = 4, column = 0, columnspan = 2,sticky = W)
    # Метка для выбора части тела
        Label(self,
              text = "Часть тела:",
              ).grid(row = 5, column = 0, sticky = W)
    # Текстовое поле ввода имени
        self.first_name = Entry(self)
        self.first_name.grid(row = 1, column = 1, columnspan = 2, sticky = W)
    # текстовое поле ввода существительного
        self.noun = Entry(self)
        self.noun.grid(row = 2, column = 1, columnspan = 2, sticky = W)
    # текстовое поле 
        self.verb = Entry(self)
        self.verb.grid(row=3, column = 1, columnspan = 2, sticky = W)
    # флажок со словом нетерпеливый
        self.is_impat = BooleanVar() 
        Checkbutton(self,
                    text = "нетерпеливый",
                    variable = self.is_impat
                    ).grid(row = 4, column = 1, sticky = W)
    # флажок со словом радостный
        self.is_glad = BooleanVar()
        Checkbutton(self,
                    text = "радостный",
                    variable = self.is_glad
                    ).grid(row = 4, column = 2, sticky = W)
    # флажок со словом пронизывающий
        self.is_piercing = BooleanVar()
        Checkbutton(self,
                    text = "пронизывающий",
                    variable = self.is_piercing
                    ).grid(row = 4, column = 3, sticky = W)
    # переменная, содержащая название одной из частей тела
        self.body_part = StringVar()
        self.body_part.set(None)
    # переключатель с названиями частей тела
        body_parts = ["пупок", "большой палец ноги", "продолговатый мозг"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part,
                        value = part
                        ).grid(row = 5, column = column, sticky = W)
            column +=1
    # кнопка отсылки данных
        Button(self,
               text = "Получить рассказ",
               command = self.tell_story
               ).grid(row = 6, column = 0, columnspan = 2, sticky = W)
    # текстовое поле, для получения данных
        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 7, column = 0, columnspan = 6)
    def tell_story(self):
        """ заполняет текстовую область историей на основе полученных данных """
        # забираем данные из GUI
        person = self.first_name.get()
        noun = self.noun.get()
        verb = self.verb.get()
        adjectives = ""
        if self.is_impat.get():
            adjectives += "нетерпиливое, "
        if self.is_glad.get():
            adjectives += "радостное, "
        if self.is_piercing.get():
            adjectives += "пронизывающее"
        body_part = self.body_part.get()
        # создание рассказа
        story = f"""Знаменитый путешественник {person}
уже совсем отчаялся довершить дело всей своей жизни - поиск затерян-
ного города, в котором, по легенде, обитали {noun.upper()}, 
но однажды {noun} и {person} столкнулись лицом к лицу.
мощное, {adjectives} ни с чем не сравнимое чувство
охватило душу путешественника.
После стольких лет поисков цель была наконец достигнута.
{person} ощутил, как на его {body_part} скатилась слезинка.
И тут внезапно {noun} перешли в атаку,
bи путешественник был ими мгновенно сожран.
Мораль ? Если задумали {verb}, надо делать это с осторожностью."""
        # вывод рассказа на экран
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)
# основная часть
root = Tk()
root.title("Сумашедший сказочник")
app = Application(root)
root.mainloop()
        
            
                    
        
        
        

        