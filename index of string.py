# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 19:39:32 2020

@author: JYOTI
"""


str1 = ("What we think we become, we are python programmers")
length = len( str1) 
num = "we"
res = [i for i in range(length) if str1.startswith(num, i)]
print("we at indices:",res)




#for each in str1:
    #if each == "w":
       # a = str1.index("we")
       # print(a)
#else:
    #print("no we in the string")
        

        
#str2 = "jyotiG"
#b = str2.islower()
#print(b)
        
