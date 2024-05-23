def print_fibonacci(length):
    fib_seq = []
    
    if length > 0:
        fib_seq.append(0)  # Add the first Fibonacci number
    if length > 1:
        fib_seq.append(1)  # Add the second Fibonacci number
        
    for i in range(2, length):
        next_value = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_value)
    
    print(fib_seq)


print_fibonacci(10)
