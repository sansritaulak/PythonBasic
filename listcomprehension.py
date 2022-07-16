#making a list of even numbers from the numbers list
numbers = [1,2,3,4,5,6,7]
even = [i for i in numbers if i%2 == 0]
print(even)