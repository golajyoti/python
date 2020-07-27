# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 22:11:31 2020

@author: JYOTI
"""


list1 = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
list1.sort()
print("sorted list is:",list1)
length = len(list1)
for i in range(0,length-1,1):
    if list1[0] == 0:
        list1.append(list1.pop(list1[0]))
print("all the 0's at the end",list1)

            