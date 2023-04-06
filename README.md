# LAB - CLASS 02

## Project : Modules and Testing
### Author: Doha Khamaiseh

### Setup :
*I installed .venv and activated it by using these commands: python3 -m venv .venv, source .venv/bin/activate  , also store the dependencies in  requirements file by using this command: pip freeze > requirements.txt*


### I run my code using this command on terminal : pytest after installing it by using this command : pip install pytest so we can test our code

### Tests :

*I will explain here a case from test cases for each function I wrote :*
1. fibonacci function :
   *we store the returned value from the Fibonacci function in the actual variable and compare it with what we expect, the returned value is the value that n (refer to the index in the series) refers to, so if n=0 that actual value should be 0 and we expect that so we will get pass test case, and so on for all values in the series*
2. lucas function  :
   *we store the returned value from the Lucas function in the actual variable and compare it with what we expect, the returned value is the value that n (refer to the index in the series) refers to, so if n=0 that actual value should be 2 and we expect that so we will get pass test case, and so on for all values in the series*
3. Sum_series function :
   *we store the returned value from the sum series function in the actual variable and compare it with what we expect, the returned value is the value that n (refer to the index in the series) refers to with respect to the base case, so if we call the function without passing the base case it by default will be the base case for Fibonacci and if n=0 the actual value should be 2 and we expect that so we will get pass test case, else if the user sent the base case = 2,1 this will call the  Lucas function else, we will return the summation of two series*

[Pull Request Link](https://github.com/DohaKhamaiseh/math-series)