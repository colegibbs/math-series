from math_series.series import fibonacci, lucas

def test_fibonacci_n_one():
  actual = fibonacci(1)
  expected = 1
  assert actual == expected

def test_fibonacci_n_zero():
  actual = fibonacci(0)
  expected = 0
  assert actual == expected

def test_fibonacci_n_two():
  actual = fibonacci(2)
  expected = 1
  assert actual == expected

def test_fibonacci_n_twelve():
  actual = fibonacci(12)
  expected = 144
  assert actual == expected

def test_lucas_n_zero():
  actual = lucas(0)
  expected = 2
  assert actual == expected

def test_lucas_n_one():
  actual = lucas(1)
  expected = 1
  assert actual == expected

def test_lucas_n_two():
  actual = lucas(2)
  expected = 3
  assert actual == expected

def test_lucas_n_ten():
  actual = lucas(10)
  expected = 123
  assert actual == expected
  
