d = {"apple":50, "banana":12, "orange":25}
d["apple"]       #key output
print(d)  
d["papaya"]=20   #adding
print(d)
del d["papaya"]  #deleting
print(d) 

for key in d:
  print("Fruit : ",key,"Quantity : ",d[key])

''''for k,v in d.items():
    print("Fruit : ",k,"Quantity : ",v)
'''
print("apple" in d)
d.clear()     #deletes everything from the dictionary 
print(d)