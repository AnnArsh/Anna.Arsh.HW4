
def palindrome_numbers(x, y):
    for i in range(x, y + 1):
        a = str(i)
        b = a[-1::-1]
        if a == b:
            print(a, end=' ')


(palindrome_numbers(13000, 13500))
