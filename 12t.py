# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
import math

from random import randint


def calculate(x, y):
    D = x*x + 4*y  # считаем дискриминант
    if D > 0:  # если дискриминанат > 0 - два корня
        sq = math.sqrt(D)/2
        p = x/2
        x = p-sq
        y = p+sq
        return x, y
    else:
        exit('invalid data')
    
def main():
    b = int(input('Enter sum: '))
    c = -int(input('Enter mul: '))
    print(calculate(b, c))

main()
