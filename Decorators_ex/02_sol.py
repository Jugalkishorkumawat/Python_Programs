def debug(func):
    def wrapper(*args,**kwargs):
        args_value = '- '.join(repr(a) for a in args)
        kwargs_value = ', '.join(f"{k}={v!r}" for k,v in kwargs.items())
        print(f"Calling {func.__name__} with arguments: {args_value}, {kwargs_value}") 
        return func(*args,**kwargs)
        
    return wrapper





@debug 
def greet(name,greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice",greeting="Good morning")  # Output: Hello, Alice!    