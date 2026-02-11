print("Welcome to the Quiz Game!")
score = 0
player = input("Do you want to play? (yes/no) ")
if player.lower() != "yes":
    print("Maybe next time!")
    exit()
else:
    print("Great! Let's get started!")

answer = input("what is the capital of india? ")
if answer.lower() =="delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Delhi.")
    
answer = input("what is the national animal of india? ")
if answer.lower() =="tiger":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Tiger.")
    
answer = input("what is the national bird of india? ")
if answer.lower() =="peacock":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Peacock.")
            
answer = input("what is the national flower of india? ")
if answer.lower() =="lotus":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Lotus.")            
        
answer = input("what is the national anthem of india? ")
if answer.lower() =="jana gana mana":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Jana Gana Mana.")   
    
print("Your final score is: " + str(score) + "/5")
print("you got", (score/5)*100, "%")
print("Thanks for playing!")         