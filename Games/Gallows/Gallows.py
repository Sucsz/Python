# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:22:07 2019

@author: sucsz
"""

#Висилица
import random
HANGMAN = (
        """
        ------
        |    |
        |
        |
        |
        |
        |
        |
        |
    -----------
        """,
        """
        ------
        |    |
        |    0
        |
        |
        |
        |
        |
        |
    -----------
        """,
        """
         ------
        |    |
        | |--O
        |
        |
        |
        |
        |
        |
    -----------
        """,
        """
         ------
        |    |
        | /--O--\
        |
        |
        |
        |
        |
        |
    -----------
        """,
        """
         ------
        |    |
        | /--O--\
        |    |
        |
        |
        |
        |
        |
    -----------
        """,
        """
         ------
        |    |
        | /--O--\
        |    |
        |    |
        |
        |
        |
        |
    -----------
        """,
        """
         ------
        |    |
        | /--O--\
        |    |
        |    |
        |   |
        |  |
        | _
        |
    -----------
        """,
        """
         ------
        |    |
        | /--O--\
        |    |
        |    |
        |   | \
        |  |   \
        | _     _
        |
    -----------
        """
        )
MAX_wrong = len(HANGMAN) - 1
WORDS = ("яблоко","школа","институт","полиция","учеба")
word = random.choice(WORDS) # слово для отгадывания
secret_word = "-" * len(word) #по одному дефису на каждую букву, которую нужно отгадать
wrong = 0 # количество ошибок, сделанных игроком
used = [] #Количество букв, использованных игроком
print("\nДобро пожаловать в игру виселица, желаю удачи")
#Начало программы
while (secret_word != word) and (wrong< MAX_wrong):
    print(HANGMAN[wrong])
    print("\n Вы уже предлагали следующие буквы:",used)
    print("\nОтгаданное вами слово сейчас выглядит так:\n",secret_word)
    answer = input("\тВведите букву: ")
    answer=answer.lower()
#Новая буква
    while answer in used:
        print("Вы уже предлагали такую букву\n")
        answer = input("\nВведите букву снова: ")
    answer = answer.lower()
    used.append(answer)
#Проверка наличия буквы в загаданном слове
    if answer in word:
        print("Да! Буква ",answer," есть в слове!")
#Формирование измененного слова
        new = ""
        for i in range(len(word)):
            if answer == word[i]:
                new += answer
            else:
                new += secret_word[i]
        secret_word = new
    else:
        print("\nК сожалению буквы ",answer," в слове не обнаружилось")
        wrong += 1
if wrong == MAX_wrong:
    print(HANGMAN[wrong])
    print("\n Вас повесили!")
else:
    print("Вы отгадали слово!")
print("Загаданное слово: ",word)
input("нажмите Enter, чтобы выйти")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


