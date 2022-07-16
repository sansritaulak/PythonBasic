#making a list of even numbers from the numbers list
s = set([1,2,3,4,5,6,7])
even = {i for i in s if i%2 == 0}
print(even)