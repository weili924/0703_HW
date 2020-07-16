# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 15:42:46 2020

@author: scott
"""


fstream1 = open("c:\pythontest\HW2.txt", mode= "w")  #取代先前資料
print("姓名 : ", file=fstream1) 
print("生日 : ", file=fstream1) 
print("年齡 : ", file=fstream1) 
fstream1.close()