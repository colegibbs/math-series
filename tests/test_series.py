from math_series.series import fibonacci

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
