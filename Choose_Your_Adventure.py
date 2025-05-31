name = input("Type your name: ")
print("Welcome", name, "to this adventure!") # type: ignore

answer = input("You are on a dirt road, it has come to an end and you can go left or right? Which way do you want to go? ")

if answer.lower() == "left":
    answer = input("You come to a river, you can walk around it or swim across?  Type walk to walk around or swim to swim across: ")

    if answer.lower() == "walk":
        print("You walked for many miles and ran out of water. You lose!")          

    elif answer.lower() == "swim":
        print("You swam across and realize that it is a never ending story. You fly off with Falcor and win!")          
elif answer.lower() == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or go back? Type 'cross' to cross the bridge or 'back' to go back: ")
    
    if answer.lower() == "back":
        print("You go back and lose!")          

    elif answer.lower() == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to them or run away? Type 'talk' to talk or 'run' to run away: ")
        
        if answer.lower() == "talk":
            print("You talk to the stranger and they give you gold. You win!")

        elif answer.lower() == "run":
            print("You run away and a chase is on. Do you want to hide or keep running? Type 'hide' to hide or 'keep' to keep running: ")
            if answer.lower() == "hide":
                print("You hide and the stranger loses you. You win!")
        
            elif answer.lower() == "keep":
                print("You keep running and get caught by the stranger. You lose!")
        
else:
    print("Not a valid option. You lose!")