# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 00:02:24 2020

@author: scott
"""


input1 = input("攝氏轉華氏請輸入A 華氏轉攝氏請輸入B，請輸入 : ")
input2 = eval(input("請輸入溫度:"))
if input1 == "A":
    input2 = (input2 + 32) * 9 / 5
else :
    input2 = (input2 - 32) * 5 / 9
print(input2)