num = int(input("Enter a no.: "))

while num > 0:
    dig = num % 10
    num = num // 10
    print(dig, end='')
    