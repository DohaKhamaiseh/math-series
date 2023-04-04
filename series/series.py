def fibonacci(n):
 if (n==0): return 0
 elif (n==1): return 1
 else :
  return fibonacci(n-1)+ fibonacci(n-2)
  

def lucas (n):
 if (n==0): return 2
 elif (n==1): return 1
 else :
  return lucas(n-1)+ lucas(n-2)

def sum_series(n,c1=0,c2=1):
 if(c1==0 and c2==1): 
  return  fibonacci(n) 
 else:
  return lucas(n)


  