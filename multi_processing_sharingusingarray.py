import multiprocessing
import numbers

def calc_square(numbers,result):
    for idx, n in enumerate(numbers):
        result[idx] = n*n
       
if __name__ == "__main__":
  numbers = [2,3,8,9]
  result = multiprocessing.Array('i',4)
  p1 = multiprocessing.Process(target = calc_square , args = (numbers, result))

  p1.start()
  p1.join()
  
  print(result[:])