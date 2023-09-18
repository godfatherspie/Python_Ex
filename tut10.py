list1 = [10,20,33,41,50]
list2 = [20,40,60,70,89]
res_list = []

for i in list1:
    if i % 2 != 0:
        res_list.append(i)

for j in list2:
    if i % 2 == 0:
        res_list.append(j)

print("The new list is: "+str(res_list))