# Посчитать сумму цифр любого целого или вещественного числа. Через строку решать нельзя.

import math 
n = int(input('write a number'))
summ = 0
while n > 0:
    summ += n%10
    n = math.floor(n/10)
print(summ)
