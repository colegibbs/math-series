from math_series.series import fibonacci, lucas, sum_series

######################################
###### fibonacci() tests ##############
######################################

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

######################################
###### lucas() tests ##############
######################################

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

######################################
###### sum_series() tests ##############
######################################

def test_sum_series_zero_none_none():
  actual = sum_series(0)
  expected = 0
  assert actual == expected

def test_sum_series_one_none_none():
  actual = sum_series(1)
  expected = 1
  assert actual == expected

def test_sum_series_2_none_none():
  actual = sum_series(2)
  expected = 1
  assert actual == expected
  
def test_sum_series_twelve_none_none():
  actual = sum_series(12)
  expected = 144
  assert actual == expected

def test_sum_series_zero_two_one():
  actual = sum_series(0, 2, 1)
  expected = 2
  assert actual == expected

def test_sum_series_one_two_one():
  actual = sum_series(1, 2, 1)
  expected = 1
  assert actual == expected

def test_sum_series_two_two_one():
  actual = sum_series(2, 2, 1)
  expected = 3
  assert actual == expected

def test_sum_series_ten_two_one():
  actual = sum_series(10, 2, 1)
  expected = 123
  assert actual == expected

def test_sum_series_two_five_seven():
  actual = sum_series(2, 5, 7)
  expected = "Only Fibonacci and Lucas series are suppored."
  assert actual == expected