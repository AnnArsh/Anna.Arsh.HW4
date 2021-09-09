def prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False


number = int(input())
for i in range(2, number):
    if prime_number(i) is not False and prime_number(number - i) is not False:
        print(i, number - i)
        break
