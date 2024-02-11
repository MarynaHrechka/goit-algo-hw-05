def caching_fibonacci():
    cache = dict()
    def fibonacci(n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n in cache.keys():
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci


fib = caching_fibonacci()
print(fib(10))
print(fib(15))
