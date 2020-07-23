# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:32:36 2020

@author: JYOTI
"""

num = int(input("Enter the number to check weathe1r its prime or not:"))
for i in range(2, num, 1):
    b = num % i
    if b == 0:
        print(num, "is not a prime number")
        break
else:
         print(num, "is a prime number")





        
