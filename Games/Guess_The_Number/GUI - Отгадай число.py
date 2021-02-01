# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:41:00 2020

@author: sucsz
"""

# Отгадай число с графическим интерфейсом 

from tkinter import*
import random
class Application(Frame):
    """ GUI-приложение, позволяющее угадывать загаданное компьюетром число """
    number = random.randint(1,100)
    def __init__(self,master):
        """ инициализирует рамку """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """ создает элементы управления: несколько меток-инструкций и одну строку
        для пользовательского ввода, одну строку для вывода"""
        # Поясняющая метка к программе
        Label(self,
              text = """ Компьютер загадал число(1..100) и, вы, 
  конечно же, сможете его отгадать! """
              ).grid(row = 0, rowspan = 2, column = 0, columnspan = 3, sticky = W )
        
        # Метка, инструкция, запрашивающая пользователский ввод
        Label(self,
              text = "Введите число",
              ).grid(row = 2, column = 0, sticky = W)
        # Поле для пользовательского ввода 
        self.input = Entry(self)
        self.input.grid(row = 2, column = 1, sticky = W)
        # кнопка, позволяющая узнать результат
        Button(self,
               text = "Узнать результат",
               command = self.check
               ).grid(row = 3, column = 0, columnspan = 3, sticky = W)
        # Метка инструкция, поясняющая, где будет результат
        Label(self,
              text = "Ваше число оказалось"
              ).grid(row = 4, column = 0, sticky = W)
        # Поле вывода
        self.output = Entry(self)
        self.output.grid(row = 4, column = 1, sticky = W)
    def check(self):
        #проверяет введенное пользователем число
        input_number = int(self.input.get())
        if input_number > Application.number:
            self.output.delete(0, END)
            self.output.insert(0, "больше, попробуйте еще")
            self.input.delete(0, END)
        elif input_number < Application.number:
            self.output.delete(0, END)
            self.output.insert(0, "меньше, попробуйте еще")
            self.input.delete(0, END)
        else:
            self.output.delete(0, END)
            self.output.insert(0, "тем самым числом!")
            self.input.delete(0, END)
            Application.number = random.randint(1, 100)
root = Tk()
root.title("Отгадай число!")
root.geometry("270x120")
app = Application(root)
root.mainloop()
            