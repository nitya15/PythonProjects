import random
print("Do you wanna play \"rock paper scissors\" (Yes or No) ?")
w=input()
while(w=="Yes"):
        print("Let's play rock paper scissors")
        print("choose either rock or paper or scissors")
        t=input()
        n=random.randrange(0,3)
        if(n==0):
            result="rock"
        elif(n==1):
            result="paper"
        else:
            result="scissors"
        print("computer chooses:"+result)
        if t=="rock" or t=="ROCK" or t=="Rock":
            if result==t:
                print("It's a tie!")
            elif result=="paper":
                print("Computer wins !")
            elif(result=="scissors"):
                print("You win !")
        elif t=="paper" or t=="PAPER" or t=="Paper":
            if result==t:
                print("It's a tie!")
            elif result=="scissors":
                print("Computer wins !")
            elif(result=="rock"):
                print("You win !")
        elif t=="scissors" or t=="Scissors" or t=="SCISSORS":
            if result==t:
                print("It's a tie!")
            elif result=="rock":
                print("Computer wins !")
            elif(result=="paper"):
                print("You win !")
        print("Do you wanna play \"rock paper scissors\" (Yes or No) ?")
        w=input()        
        
        
            
        
    
        
        
    
    
