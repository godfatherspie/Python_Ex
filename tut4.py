#Remove first n characters from a string

def remove_char():
    str1 = input("Enter a string: ")
    n = int(input("Enter the no. of characters you wish to remove: "))
    if n > len(str1):
        print("Invalid Input, try again")
    else:
        print("New string: "+str(str1[n:]))

remove_char()
