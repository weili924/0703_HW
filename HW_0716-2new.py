# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 00:09:02 2020

@author: scott
"""

#請輸入西元出生年，請以1900年後為主，輸入完後，會出現對應的生肖年，如: 1900年 為 老鼠。
year = eval(input("請輸入出生年份:"))
rem = year  % 12
if rem == 4:
    print("生肖為:鼠")
elif rem == 5:
    print("生肖為:牛")
elif rem == 6:
    print("生肖為:虎")
elif rem == 7:
    print("生肖為:兔")
elif rem == 8:
    print("生肖為:龍")
elif rem == 9:
    print("生肖為:蛇")
elif rem == 10:
    print("生肖為:馬")
elif rem == 11:
    print("生肖為:羊")
elif rem == 1:
    print("生肖為:雞")
elif rem == 2:
    print("生肖為:狗")
elif rem == 3:
    print("生肖為:豬")
else:
    print("生肖為:猴")
