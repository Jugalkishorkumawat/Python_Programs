age  = input("Enter your age: ")
age = int(age)
if age < 13:
    print("child")
elif age in range(13, 20):
    print("teenager")
elif age in range(20, 65):
    print("adult")
else:
    print("elder")
# --- IGNORE ---

