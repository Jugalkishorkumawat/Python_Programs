def sum_all(*args):
    # print(*args)  # Output: (1, 2, 3, 4)
    # print(type(args))  # Output: <class 'tuple'>
    # print(args[0])  # Output: 1
    print(args) 
    for i in args:
        print(i*2)


    """Returns the sum of all arguments."""
    return sum(args)
print(sum_all(1, 2, 3, 4))  # Output: 10
print(sum_all(5, 10, 15))    # Output: 30