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
  if n == 0:
    return nth_zero
  elif n == 1:
    return nth_one
  else:
    return sum_series((n - 1), nth_zero, nth_one) + sum_series((n - 2), nth_zero, nth_one)
