# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 20:19:03 2020

@author: sucsz
"""
somelist = [1,2,3,4,5,6,7,8]
print(somelist)
#somelist[:] = [x for x in somelist if not  somelist.index(x) == 3]
#print(somelist)
#for i in range(8):
#    somelist[i] = None
#print(somelist)
for i in somelist:
    x = int(somelist.index(i))
    #somelist[somelist.index(i)] = 1
    somelist[x] = None
print(somelist)
somelist[:] = [x for x in somelist if not  x == None]
print(somelist)

