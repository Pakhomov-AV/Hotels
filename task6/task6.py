# Написать метод, который в консоль выводит таблицу умножения. На вход метод получает число,
# до которого выводит таблицу умножения. В консоли должна появиться таблица.
# Например, если на вход пришло число 5, то получим:

# Важно:
# В последней строке между числами ровно по одному пробелу должно выводиться.
# В каждом столбце числа должны быть выровнены по правому краю.

# Решил примерно за 25 минут

def f(n):
    Array = []
    for i1 in range(1, n+1):
        Array += [[]]
        for i2 in range(1, n+1):
            Array[i1-1] += [i1*i2]
    S = ""
    E = []
    for i in Array[-1]:
        E += [len(str(i))+1]
    Column = []
    for i in range(1, n+1):
        Column += [i]
    Array = [Column] + Array
    Row = 0
    for i in Array:
        s = ""
        I = 0
        for i2 in i:
            s += (E[I]-len(str(i2)))*" "+str(i2)
            I += 1
        S += str(Row)+" "+s+'\n'
        Row += 1
    S = " "+S[1:]
    print(S)


f(4)
print()
f(5)
print()
f(7)
