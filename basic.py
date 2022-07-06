#Variables, basic operators 
location1 = "Pokhara"
location2 = "Kathmandu"
location3 = "Chitwan"
dist1_2 = 200.6
dist2_3 = 97.7
total_dist = dist1_2 + dist2_3
print("The distance between %s and %s is %fkm."%(location1,location2,dist1_2))
print("The distance between %s and %s is %fkm."%(location2,location3,dist2_3))
print("The total distance from %s to %s is %fkm"%(location1,location3,total_dist))
mph = 50
time = total_dist/mph
print("Time taken to reach %s with speed %dkm/hrs is %fhrs"%(location3,mph,time))

#strings
text = "Hello World "
print(text)
text2 = 'Hello World 2'
print(text2)
text3 = "It's a string"
print(text3)
text4 = 'Hello "World"'
print(text4)
text5 = text + text3
print(text5)
num = 19
age = "My age is "
sen = age + str(num)
print(sen)
id = '''Hello Everyone
My name is Sansrita'''
print(id)