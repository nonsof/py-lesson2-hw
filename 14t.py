# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

import math
n = int(input("write a number: "))
sq = 2
st = 0
while sq**st <= n:
    print(sq**st)
    st += 1
