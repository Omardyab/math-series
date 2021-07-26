
PR Link: https://github.com/Omardyab/math-series/pull/2

Three main cases: 
Fibonacci: a sequence is generated based on the summation of two Fibonacci functions. 
It is implemented using recursion with 2 cases, 0 and 1.

sum_series: sequence is generated based on the summation of the first two functions, which are  0 and 1, this is by default.
  Lucas  if the two number => 2 and 1,
otherwise, a sequence is generated based on the two numbers as recived.

Lucas:a sequence is generated based on the summation of the first two Lucas functions. 
It is implemented using recursion with 2 cases, 2 and 1.

User Acceptance Tests: 

Fibonacci test cases:
    0 => 0
    1 => 1
    8 => 21
    -1 => "Input is not valid"
    "x" => "Input is not valid"

sum_series test cases:
    8 => 21
    8,2,1 => 47
    5,5,5 => 40
    3,-2,-5 => -12
    "z",5,6 => "Input is not valid"

Lucas test cases:
    0 => 2
    1 => 1
    10 => 123
    -2 => "Input is not valid"
    "Y" => "Input is not valid"

