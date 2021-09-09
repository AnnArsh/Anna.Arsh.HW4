number = int(input())
for i in range(1, number+1, 2):
    x = '*' * i
    print((number - i)//2 * " ", x, (number - i)//2 * " ")
