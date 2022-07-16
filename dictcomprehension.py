city= ["Pokhara","Delhi","New York"]
country = ["Nepal","India","USA"]
z = zip(city,country)
for a in z:
  print (a)

d = {city:country for city,country in zip(city,country)}
print (d)