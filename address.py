#writing record as a json format
book = {}
book['Ram'] = {
    'Name' : 'Ram',
    'Address' : 'Pokhara, Nepal'
}
book['Hari'] = {
    'Name' : 'Hari',
    'Address' : 'Jumla, Nepal'
}

import json
s=json.dumps(book)
with open ("/home/sansrita/Desktop/Python/address.txt","w") as f:
    f.write(s)

#printing the record from the .txt file
f=open("/home/sansrita/Desktop/Python/address.txt","r") 
s= f.read()
print(s)
print(type(s))
import json
l= json.loads(s)
print(l)
print(type(l))
print(l['Hari'])
print(l['Hari']['Address'])

#print all the record
for person in l:
    print(l[person])