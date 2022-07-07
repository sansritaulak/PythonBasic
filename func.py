def total(exp):
  total = 0
  for item in exp:
    total = total + item
  return total

list1 = [1200,3000,4500]
list2 = [200,600,450]

list1_total = total(list1)
list2_total = total(list2)

print ("Total of List 1 : ", list1_total)
print ("Total of List 2 : ", list2_total)