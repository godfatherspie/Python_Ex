#Check if the first and last number of a list is the same

def t_f(list1):
    print("Given list: "+str(list1))

    num1 = list1[0]
    num2 = list1[-1]

    if num1 == num2:
        print("True")
    else:
        print("False")

x = [12,59,49,5,12]
t_f(x)
