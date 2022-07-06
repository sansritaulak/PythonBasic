#Write a program that asks the user to enter a number and then tell wheather the number is odd or even.

# num = int(input("Enter a Number : "))
# #The function int() is used to convert a string into an integer.
# if num%2 == 0 :
#   print("The number is even.")
# else:
#   print("The number is odd.")

#Write a program to check which Grade she obtained

per = int(input("Enter your percentage : "))
if per >= 90 and per <= 100:
  print("A+")
elif per >= 80 and per < 90:
  print("A")
elif per >= 70 and per < 80:
  print("B+")
elif per >= 60 and per < 70:
  print("B")
elif per >= 50 and per < 60:
  print("C+")
elif per >= 40 and per < 50:
  print("C+")
elif per >= 0 and per < 40:
  print("Failed")
else:
  print("Enter valid percentage")