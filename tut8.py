#Print the following pattern
#1 
#2 2 
#3 3 3 
#4 4 4 4 
#5 5 5 5 5

rows = 6

for i in range(rows):
    for j in range(i):
        print(i, end='')
    print('')
