# recursive, inefficient Fibonacci

def fib1(n):
    if n < 2:
        # base case for n = 0 or 1
        return 1
    else:
        # recursive case
        return fib1(n-1) + fib1(n-2)

# recursive, efficient Fibonacci with memoisation

fib = {}  # dictionary to record previous Fibonacci numbers

def fib2(n):
    global fib
    if n < 2:
        # base case for n = 0 or 1
        return 1
    else:
        # recursive case
        if n-1 not in fib:
            fib[n-1] = fib2(n-1)
        if n-2 not in fib:
            fib[n-2] = fib2(n-2)
        return fib[n-1] + fib[n-2]

