#Print characters from a string that are present at an even index number

str1 = input("Enter a string: ")
print("Length of string: "+str(len(str1)))

for i in range(0,len(str1)-1,2):
    print("Characters at even index "+str(str1[i]))
