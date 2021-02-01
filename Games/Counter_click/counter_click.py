# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 00:50:13 2020

@author: sucsz
"""

# Счетчик щелчков
# Демонстрирует связанные события 
from tkinter import *
class Application(Frame):
    """ GUI-приложение, которое подсчитывает количество нажатий кнопки """
    def __init__(self, master):
        """ Инициализирует рамку """
        super(Application,self).__init__(master)
        self.grid()
        self.bttn_clicks = 0 # количество нажатий
        self.create_widget()
    def create_widget(self):
        self.bttn = Button(self, text = "Количество щелчков: 0")
        self.bttn["command"] = self.update_count
        self.bttn.grid()
    def update_count(self):
        """ Увеличивает количество нажатий на ежиницу и отображает его """
        self.bttn_clicks += 1
        self.bttn["text"] = f"Количество щелчков:{str(self.bttn_clicks)} "
# Основная часть
root = Tk()
root.title("Счетчик щелчков")
root.geometry("200x100")
app = Application(root)
root.mainloop()
