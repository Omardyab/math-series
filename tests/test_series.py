from math_series.series import fibonacci,sum_series,lucas

"""
Fibonacci test cases:
    0 => 0
    1 => 1
    8 => 21
    -1 => "Input is not valid
    "x" => "Input is not valid
"""

def test_fib_zero(): 
    expected=0
    actual= fibonacci(0)
    assert expected==actual
    
def test_fib_one(): 
    expected=1
    actual= fibonacci(1)
    assert expected==actual

def test_fib_eight(): 
    expected=21
    actual= fibonacci(8)
    assert expected==actual

def test_fib_Negative(): 
    expected="Input is not valid"
    actual= fibonacci(-1)
    assert expected==actual

def test_fib_letter(): 
    expected="Input is not valid"
    actual= fibonacci('x')
    assert expected==actual
"""
Lucas test cases:
    0 => 2
    1 => 1
    10 => 123
    -2 => "Input is not valid"
    "Y" => "Input is not valid"
"""
def test_luc_zero():
    expected = 2
    actual = lucas(0)
    assert actual == expected

def test_luc_one():
    expected = 1
    actual = lucas(1)
    assert actual == expected

def test_luc_ten():
    expected = 123
    actual = lucas(10)
    assert actual == expected

def test_luc_Negative(): 
    expected="Input is not valid"
    actual= lucas(-2)
    assert expected==actual

def test_luc_letter(): 
    expected="Input is not valid"
    actual= lucas('Y')
    assert expected==actual


"""
sum_series test cases:
    8 => 21
    8,2,1 => 47
    5,5,5 => 40
    3,-2,-5 => -12
    "z",5,6 => "Input is not valid"
"""
def test_sum_series_eight():
    expected=21
    actual=sum_series(8)
    assert expected==actual

def test_sum_series_eight_two_one():
    expected=47
    actual=sum_series(8,2,1)
    assert expected==actual

def test_sum_series_triple_five():
    expected=40
    actual=sum_series(5,5,5)
    assert expected==actual

def test_sum_series_Negative(): 
    expected=-12
    actual=sum_series(3,-2,-5)
    assert expected==actual

def test_sum_series_letter(): 
    expected="Input is not valid"
    actual=sum_series("z",5,6)
    assert expected==actual


