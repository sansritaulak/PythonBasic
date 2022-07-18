#To find time taken in a function without decorators
import time 

def calc_square(numbers):
  start = time.time()
  result = []
  for number in numbers:
    result.append(number*number) 
    end = time.time()
    print ("calc_square took " +str((end-start)*1000) + "mil sec")
    return result

def calc_cube(numbers):
  start = time.time()
  result = []
  for number in numbers:
    result.append(number*number*number) 
    end = time.time()
    print ("calc_cube took " +str((end-start)*1000) + "mil sec")
    return result
    
array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)



#To find time taken in a function using decorators
import time 

def time_it(func):
  def wrapper(*args, **kwargs):
    start =time.time()
    result = func(*args,*kwargs)
    end = time.time()
    print(func.__name__ + " took "+str((end-start)*1000) +"mili seconds")
  return wrapper

@time_it                                #calling the decorator
def calc_square(numbers):
  result = []
  for number in numbers:
    result.append(number*number) 
    return result

@time_it                                #calling the decorator
def calc_cube(numbers):
  result = []
  for number in numbers:
    result.append(number*number*number)
    return result

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)