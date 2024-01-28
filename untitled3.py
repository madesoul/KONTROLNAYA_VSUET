def order_numbers(first, second):

    if first < second:

        for num in range(first, second+1):

            print(num, end=" ")

        else:

            for num in range(first, second-1, -1):

                 print(num, end=" ")

a = int(input("Введите первое число: "))

b = int(input("Введите второе число: "))

order_numbers(a, b)



A,B=[int(input()) for i in range(2)]

for i in range(A, B+1):

    print(i)

else:

    for i in range(A, B-1, -1):

        print(i)


a = int(input("Введите A: "))

b = int(input("Введите B: "))

if a < b:

    for i in range(a, b+1):

        print(i, end=' ')

else:

    for i in range(a, b-1, -1):

        print(i, end=' ')
