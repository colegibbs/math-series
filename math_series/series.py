def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  else: 
    return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
  if n == 0:
    return 2
  elif n == 1:
    return 1
  else:
    return lucas(n - 1) + lucas(n - 2)

def sum_series(n, nth_zero = 0, nth_one = 1):
  if (nth_zero == 0 and nth_one == 1) or (nth_zero == 2 and nth_one == 1): 
    if nth_zero == 0 and nth_one == 1:
      return fibonacci(n)
    else:
      return lucas(n)
  else:
    return "Only Fibonacci and Lucas series are suppored."