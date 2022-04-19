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