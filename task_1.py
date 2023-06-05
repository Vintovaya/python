# Винтовая Дария 44-22-122 задание 1
import math
import sys


def main(*args):
    try:
        x = float(args[0][0])
        if x < 0.5:
            return math.sqrt(math.sin(x) + math.cos(x) ** 2)
        else:
            return math.exp(x ** 3 * (math.sin(3*x)))
    except:
        return "Произошла ошибка"

print(main(sys.argv[1:]))