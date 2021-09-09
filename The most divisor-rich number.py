def divisors(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
    return count


a = int(input())
b = int(input())
max_div_num = a
for i in range(a, b+1):
    if divisors(i) > divisors(max_div_num):
        max_div_num = i
print(max_div_num)
