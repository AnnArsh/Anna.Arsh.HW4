lst = []
n = int(input())
k = int(input())
for i in range(n):
    lst.append(int(input()))
for j in range(k):
    x = lst[-1]
    for i in range(n-1, 0, -1):
        lst[i] = lst[i-1]
    lst[0] = x
print(lst)
