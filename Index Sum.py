n = int(input())
m = int(input())
A = []
Ind = []
sum_of_el = 0
for i in range(n):
    A.append(int(input()))
for i in range(m):
    Ind.append(int(input()))
for j in Ind:
    sum_of_el += A[j]
print(sum_of_el)

# def sum_list_elements(lst1, lst2):
#     x = 0
#     for i in lst2:
#         x += lst1[i]
#     return x
#
#
# n = int(input())
# m = int(input())
# A = []
# Ind = []
# sum_of_el = 0
# for i in range(n):
#     A.append(int(input()))
# for i in range(m):
#     Ind.append(int(input()))

# print(sum_list_elements(A, Ind))
