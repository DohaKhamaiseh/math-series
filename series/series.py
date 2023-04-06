def fibonacci(n):
   '''
   this function will produce a Fibonacci series
    which look like this: 0,1,1,2,3,5,8,13...

    the  conditions below will check the base case for the series which is 0 in index 0 and 1 in index 1
    we did this to avoid an infinite loop, n refer to the index of the wanted element in the series
  '''
   if (n == 0):
     return 0
   elif (n == 1):
     return 1
   else:
    return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
     '''
   this function will produce a lucas series
    which look like this: 2,1,3,4,7,11...

    the  conditions below will check the base case for the series which is 2 in index 0 and 1 in index 1
    we did this to avoid an infinite loop, n refer to the index of the wanted element in the series
  '''
     if (n == 0):
        return 2
     elif (n == 1):
        return 1
     else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, c1=0, c2=1):
        '''
this function will call a Fibonacci series
    which look like this: 2,1,3,4,7,11...
    when the user doesn't send  the optional parameters by calling (they have default values)

    and calling a Lucas series if the user sent the optional parameters by calling with values c1=2, c2=1
    otherwise, it will call the summation of both series
  ''' 
        if (c1 == 0 and c2 == 1):
           return fibonacci(n)
        elif (c1 == 2 and c2 == 1):
          return lucas(n)
        else:
           return fibonacci(n) + lucas(n) 
    
