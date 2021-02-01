# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:39:06 2019

@author: sucsz
"""
#Анаграмма
import random
WORDS=("питон",
       "программирование",
       "учеба",
       "институт",
       "общага",
       "Гистология")
word=random.choice(WORDS)
correct=word
jumble=""
while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word=word[:position]+word[position+1:]
print(jumble, "- вот вам анаграмма, попробуйте ее разгадать")
answer=input("Введите ваш вариант ").lower()

while answer!=correct:
    print("К сожалению, вы не правы")
    answer=input("\nПопробуйте снова ")
if answer==correct:
    print("Вы молодец, слово отгадано")
    