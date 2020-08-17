# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 00:33:28 2020

@author: scott
"""


#輸入三個數字，由程式由大排到小
#abc acb bac bca cab cba

a,b,c, = eval(input("請輸入三個數字 : "))
if a >= b and b >= c:
    print(a,b,c)
   
elif a < b and a >= c:
    print(b,a,c)
  
elif a >= c and b <= c:
    print(a,c,b)    
    
elif a < c and b >= c:
    print(b,c,a)

elif c > a >= b:
    print(c,a,b)
    
elif c > b > a:
    print(c,b,a)