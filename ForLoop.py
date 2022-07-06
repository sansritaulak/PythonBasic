#Store monthly expenses in a list and find out the total expense for all months

exp = [2400, 2600, 3000, 2400, 3500, 2000, 3624, 1252, 750, 1210, 940, 450]
total = 0
for item in exp:
    total = total + item
print(total)

#range()
for i in range (1,11):
    print(i)
    
#Print the month and expense of the month

exp = [2400, 2600, 3000, 2400, 3500, 2000, 3624, 1252, 750, 1210, 940, 450]
total = 0
for i in range(len(exp)):
    print("Month",i+1,"Expense",exp[i])
    total = total + exp[i]
print("Total expense",total)

#continue and break in for loop 
#make a loop to print all the even numbers till 10

for i in range(1,20):
    if i%2!=0:
        continue
    elif i>=11:
        break
    print(i)

