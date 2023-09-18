previous_num = 0
i = 1
for i in range(10):
    print("Current no. "+str(i))
    print("Previous no. "+str(previous_num))
    sum = previous_num+i
    print("Sum is: "+str(sum)) 
    previous_num = i