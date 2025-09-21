
# Banana = {
#     "Green" = "unripe",
#     "Yellow" = "ripe",
#     "Brown" = "overripe"
# }
# for color, ripeness in Banana.items():
#     print(f"A {color} banana is {ripeness}.")


fruit = "apple"
color = "white"

if fruit == "banana":
    if color == "green":
        print("The banana is unripe.")
    elif color == "yellow":
        print("The banana is ripe.")
    elif color == "brown":
        print("The banana is overripe.")
    else:
        print("Unknown color for banana.")

elif fruit == "apple":
    if color == "red":
        print("The apple is unripe.")
    elif color == "white":
        print("The apple is ripe.")
    elif color == "brown":
        print("The apple is overripe.")
    else:
        print("Unknown color for apple.")        


