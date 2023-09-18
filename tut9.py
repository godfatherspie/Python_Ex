def palindrome():
    x = input("Enter a number to check if it is palindrome or not: ")
    if str(x[::-1]) == str(x):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

palindrome()