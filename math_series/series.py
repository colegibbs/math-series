def fibonacci(n):
  '''
    This function executes the fibonacci sequence based on the parameter n. n is evaluated against the base cases of the fibonacci sequence, if neither base case is true, the fibonacci sequence is run based on n.
  '''
  
  if n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  else: 
    return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
  '''
  This function executes the lucas sequence based on the parameter n. n is evaluated against the base cases of the lucas sequence, if neither base case is true, the lucas sequence is run based on n. 
  '''
  if n == 0:
    return 2
  elif n == 1:
    return 1
  else:
    return lucas(n - 1) + lucas(n - 2)

def sum_series(n, nth_zero = 0, nth_one = 1):
  '''
  This function executes a fibonnaci/lucas style formula on the given parameters. The first parameter is the n that you wish the formula to execute on. The second is an optional base case of nth = 0. The third is an optional base case of nth = 1. If the last two arguments are ecluded, this function will execute as a fibbonaci sequence based on n. 
  '''
  if n == 0:
    return nth_zero
  elif n == 1:
    return nth_one
  else:
    return sum_series((n - 1), nth_zero, nth_one) + sum_series((n - 2), nth_zero, nth_one)
