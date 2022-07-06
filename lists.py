eat = ["Pizza","MoMo","Pasta"]
drinks = ["Juice","Coke"]

#if we want to print 1st item 
print(eat[0])

#if we want to print 1st and 2nd item
print(eat[0:2])

#To print the last item
print(eat[-1])

#If we want to add Wings in the food 
eat.append("Wings")
print(eat)

#If we want to add Chips in the 2nd position
eat.insert(1,"Chips")
print(eat)

#If we need to combine eat and drinks
items = eat + drinks
print(items)

print("Total number of items in the list is ",(len(items)))

#Check if Pasta is in the list or not 
print("Pasta" in items)