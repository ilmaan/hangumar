import random

print("    ======== H=A=N=G=M=A=N ========   ")
name=input("+++ Enter Your Name++++ \n")
print("HELLO", name ,"Welcome to the game")
print("\n")
print("You have to guess the correct word to save Umar Khalid")

l="Y"

def hang():
    word= random.choice(["caa","nrc","azaadi","enemployment","modi","bjp","chor"])
    vl="abcdefghijklmnopqrstuvwxyz"
    t=5
    gm=''
    
    while len(word)>0:
        main=""
        ms=0

        for letter in word:
            if letter in gm:
                main=main+letter
            else:
                main=main+"_"+" "
        if main==word:
            print(main)
            print("congrats for saving umar khalid ")
            break
        print("GUESS THE DAMN WORD >>>>>",main)
        gs=input()

        
        
        
        if gs in vl:
            gm=gm+gs

        else:
            print("++++wtf u entering human+++++")
            gs=input()
        if gs not in word:
            t=t-1
            if t==4:
                print("modi put fake case on him")
            if t==3:
                print("police showing brutality")
            if t==2:
                print("save him from being another Najeeb")
            if t==1:
                print("please save him")
            if t==0:
                print("congrats You forget umar and khali cooker gas pe chada dia")
                break        

while (l=="Y" or l=="y"):
    hang()
    l=input("***** WANNA PLAY AGAIN SON *****")
    print("$$$$$ THIS GAME IS DEVELOPED BY ILMAAN ZIA OF JAMIA HAMDARD  $$$$$$")

   