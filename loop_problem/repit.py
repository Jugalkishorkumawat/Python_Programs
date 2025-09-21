input_str  = "teeterabc"
for char in input_str:
    if input_str.count(char) == 1:
        print("Char is ",char)
        break
print("No unique char")


input_str  = "teeterabc"
for char in input_str:
    if input_str.count(char) == 1:
        print("Char is ",char)
        continue
