name = input("Enter your name: ")
print(f"Welcome to the Choose Your Own Adventure Game, {name}!")
answer= input("You find yourself at a crossroads. Do you want to go left or right? (enter 'left' or 'right') ")

if answer.lower() == "left":
    answer = input("You encounter a river. Do you want to swim across or build a raft? (enter 'swim' or 'raft') ")
    if answer.lower() == "swim":
        print("You try to swim across but the current is too strong. You get swept away and lose the game.")
    elif answer.lower() == "raft":
        print("You successfully build a raft and cross the river. You win the game!")

elif answer.lower() == "right":
    answer = input("You come across a dark cave. Do you want to enter the cave or keep walking? (enter 'enter' or 'walk') ")
    if answer.lower() == "enter":
        answer = input("You enter the cave and find a narrow way from where the sun light is coming. Do you want to enter or go back? (enter 'narrow' or 'Go back')")
        if answer.lower() == "narrow":
           print("you came other side of cave and got the treasure. You won the game")
        elif answer.lower() == "go back":
           print("while going back you where eaten by a tiger, You lose the game.")  
          
    elif answer.lower() == "walk":
        print("You keep walking and eventually get lost in the forest. You lose the game.")
                    
print("Thanks for playing, " + name + "!")                    

