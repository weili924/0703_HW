# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 15:45:42 2020

@author: scott
"""


fstream2 = open("c:\pythontest\HW3.txt", mode= "a") #附加資料後面
print("請輸入data : ", file=fstream2) 
fstream2.close()