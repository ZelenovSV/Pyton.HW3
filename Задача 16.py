'''Задача 16: Требуется вычислить, сколько раз встречается некоторое число X
в массиве A[1..N]. Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. В последующих  строках 
записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1'''
n = int(input("Введите количество элементов в массиве: "))
array = []
for i in range(1,n+1):
    array.append(i)
print(array)
x = int(input("Введите искомое число: "))
count = 0
for i in range(n):
    if array[i] == x:
        count += 1
print("Искомое число содержится в массиве {} раз/раза".format(count))