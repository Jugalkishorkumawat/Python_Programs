# def print_kwarga(name,power):
#     print(f"{name} has the power of {power}")
#     print("Name",name,"Power",power)
def print_kwargs(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(f"{key} : {value}")


print_kwargs(name = "ashok" , power="lazer")

print_kwargs(power="lazer",name = "ashok" ) #then output are same 
