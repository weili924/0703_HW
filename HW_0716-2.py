# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 06:07:16 2020

@author: scott
"""


#請輸入西元出生年，請以1900年後為主，輸入完後，會出現對應的生肖年，如: 1900年 為 老鼠

print("生肖年確認")
year=int(input("請输入西元年份："))
a = ["猴 " ,"雞 " ,"狗" ,"猪" ,"鼠" ,"牛" ,"虎" ,"兔" ,"龍" ,"蛇" ,"馬" ,"羊"]
b = year % 12

if a == 0:
    print('生肖為{}'.format(a[b]))
elif a == 1:
    print('生肖為{}'.format(a[b]))
elif a == 2:
    print('生肖為{}'.format(a[b]))
elif a == 3:
    print('生肖為{}'.format(a[b]))
elif a == 4:
    print('生肖為{}'.format(a[b]))
elif a == 5:
    print('生肖為{}'.format(a[b]))
elif a == 6:
    print('生肖為{}'.format(a[b]))
elif a == 7:
    print('生肖為{}'.format(a[b]))
elif a == 8:
    print('生肖為{}'.format(a[b]))
elif a == 9:
    print('生肖為{}'.format(a[b]))
elif a == 10:
    print('生肖為{}'.format(a[b]))
elif a == 11:
    print('生肖為{}'.format(a[b]))
else:
    print('計算錯誤')



