# def even_generator(n):
#     """Generate even numbers up to n (exclusive)."""
#     li = []
#     for i in range(2, n+1,2):
#         li.append(i)
#     return li
# print(even_generator(10))


def even_generator(n):
    """Generate even numbers up to n (exclusive)."""
    n=10    
    for i in range(2, n+1,2):
        yield i

for  n in even_generator(10):
    print(n)