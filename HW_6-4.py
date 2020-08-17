# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 01:11:17 2020

@author: scott
"""


a,b,c, = eval(input("請輸入三個數字 : "))
if a >= b and a >= c :
    if a >= b + c:
        print("無法組成三角形")
    else:
        print(a + b + c)

elif a < b and b >= c:
    if b >= a + c:
        print("無法組成三角形")
    else:
        print(a + b + c)
elif a < c and b < c :
   if c >= b + a:
        print("無法組成三角形")
   else:
        print(a + b + c)