#Напишите функцию, которая принимает два числа и возвращает их сумму

def summa(a,b):
    return a + b
a = int(input())
b = int(input())
res = summa(a,b)
print(f"Сумма {a} и {b} равна {res}")


#Напишите функцию, которая проверяет, является ли число простым.

def chislo(a):
    if a <= 1:
        return False
    for i in range(2,a):
        if a % i == 0:
            return False
    return True


#Напишите функцию, которая принимает список чисел и возвращает их среднее значение.

def funcia(num):
    return sum(num)/len(num)
numbers = [1,2,3,4,5]
print(funcia(numbers))
