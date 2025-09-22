def greet(name = "User"):
    return "Hello, " + name +"!"
print(greet())
print(greet("Alice"))

cube = lambda x: x**3
print(cube(3))