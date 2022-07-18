#For a given list of numbers print square and cube of every numbers(without using multithreading)
import time

def calc_square(numbers):
  for n in numbers:
    time.sleep(0.2)
    print("Square : ",n*n)
    
def calc_cube(numbers):
  for n in numbers:
    time.sleep(0.2)
    print("Cube : ",n*n*n)

arr = [2,3,8,9]

t = time.time()
calc_square(arr)
calc_cube(arr)

print("Time taken (without multithreading) : ",time.time()-t)

#For a given list of numbers print square and cube of every numbers(using multithreading)
import time
import threading

def calc_square(numbers):
  for n in numbers:
    time.sleep(0.2)
    print("Square : ",n*n)
    
def calc_cube(numbers):
  for n in numbers:
   time.sleep(0.2)
  print("Cube : ",n*n*n)

arr = [2,3,8,9]

t = time.time()

t1 = threading.Thread(target=calc_square,args=(arr,))
t2 = threading.Thread(target=calc_cube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Time taken (with multithreading): ",time.time()-t)