import random

myWin=0
compWin=0
draw =0

def startGame():
    global myWin
    global compWin
    global draw
    
    wordList=["Scissor","Paper","Rock"]
    print("======================")
    userValue=input("Select 1=Scissor or 2=Paper or 3=Rock : ")
    check_userValue=userValue.isnumeric()
    if check_userValue==True:
        userValue=int(userValue)
        if userValue>=1 and userValue<=3:
            print("======================")
            comp=random.randint(1,3)
            print("Computer choose : ",comp)
            if userValue==comp:
                print("DRAW!!!")
                print("========================")
                draw+=1
            elif userValue==1 and comp==2:
                print("***YOU WON***","\nyou =",wordList[userValue-1],"comp = ",wordList[comp-1])
                print("========================")
                myWin+=1
            elif userValue==2 and comp==3:
                print("***YOU WON***","\nyou =",wordList[userValue-1],"comp = ",wordList[comp-1])
                print("========================")
                myWin+=1
            elif userValue==3 and comp==1:
                print("***YOU WON***","\nyou =",wordList[userValue-1],"comp = ",wordList[comp-1])
                print("========================")
                myWin+=1
            else:
                print("***YOU LOSE***\n","you =",wordList[userValue-1],"comp = ",wordList[comp-1])
                print("========================")
                compWin+=1

        else:
            print("========================")
            print("Invalid Input.......\nPlease select only 1(Scissor) or 2(Paper) or 3(Rock) : ")
            startGame()
    else:
        print("========================")
        print("Invalid Input.......\nPlease select only 1(Scissor) or 2(Paper) or 3(Rock) : ")
        startGame()

def exitGame():
    global myWin
    global compWin
    global draw
    print("======================")
    print("Do you want to continue....Y/N :\n")
    str=input("")

    if str=='Y' or str=='y':
        myWin=0
        compWin=0
        draw=0
        game()
    else:
        print("Thank you for playing.........")
        exit()

def game():
    i=0
    while i<5:
        startGame()
        i+=1
    else:
        print("Final Score :")
        print("Your Score :",myWin,"\nComputer Score :",compWin,"\nDraw :",draw)
        exitGame()

game()

