import numpy as np
import random
myarray=np.array(range(9), dtype=str).reshape(3,3)
print(myarray)
numbers=[0,1,2,3,4,5,6,7,8]
print("******* CHOOSE X OR O  *******")
player_choose=input()
if player_choose=="X":
    computer_choose="O"
else:
    computer_choose="X"

def Wincondition():
    win=False
    if myarray[0,0]==myarray[0,1]==myarray[0,2]:
        win=True
        if win is True:
            return "Win"
    if myarray[1,0]==myarray[1,1]==myarray[1,2]:
        win=True
        if win is True:
            return "Win"
    if myarray[0,0]==myarray[1,0]==myarray[2,0]:
        win=True
        if win is True:
            return "Win"
    if myarray[0,1]==myarray[1,1]==myarray[2,1]:
        win=True
        if win is True:
            return "Win"
    if myarray[0,2]==myarray[1,2]==myarray[2,2]:
        win=True
        if win is True:
            return "Win"
    if myarray[0,0]==myarray[1,1]==myarray[2,2]:
        win=True
        if win is True:
            return "Win"
    if myarray[0,2]==myarray[1,1]==myarray[2,0]:
        win=True
        if win is True:
            return "Win"
    if myarray[2,0]==myarray[2,1]==myarray[2,2]:
        win=True
        if win is True:
            return "Win"




while True:
    print(f"*** Where do yo want to place your {player_choose}.Choose any of the Places {numbers}  *** ")
    Player_Chance=int(input())
    Computer_Chance=random.choice(numbers)
    if Player_Chance==0:
        myarray[0,0]=player_choose
        print(myarray)
        numbers.remove(Player_Chance)
        A=(Wincondition())
        if A:
            print("Player Win hurray!")
            break
    if Player_Chance==1:
        myarray[0,1]=player_choose
        print(myarray)
        numbers.remove(Player_Chance)
        A=(Wincondition())
        if A:
            print("Player Win hurray!")
            break
    if Player_Chance==2:
        myarray[0,2]=player_choose
        print(myarray)
        numbers.remove(Player_Chance)
        A=(Wincondition())
        if A:
            print("Player Win hurray!")
            break
    if Player_Chance==3:
        myarray[1,0]=player_choose
        print(myarray)
        numbers.remove(Player_Chance)
        A=(Wincondition())
        if A:
            print("Player Win hurray!")
            break
    if Player_Chance==4:
        myarray[1,1]=player_choose
        print(myarray)
        numbers.remove(Player_Chance)
        A=(Wincondition())
        if A:
            print("Player Win hurray!")
            break
    if Player_Chance==5:
        myarray[1,2]=player_choose
        print(myarray)
        numbers.remove(Player_Chance)
        A=(Wincondition())
        if A:
            print("Player Win hurray!")
            break
    if Player_Chance==6:
        myarray[2,0]=player_choose
        print(myarray)
        numbers.remove(Player_Chance)
        A=(Wincondition())
        if A:
            print("Player Win hurray!")
            break
    if Player_Chance==7:
        myarray[2,1]=player_choose
        print(myarray)
        numbers.remove(Player_Chance)
        A=(Wincondition())
        if A:
            print("Player Win hurray!")
            break
    if Player_Chance==8:
        myarray[2,2]=player_choose
        print(myarray)
        numbers.remove(Player_Chance)
        A=(Wincondition())
        if A:
            print("Player Win hurray!")
            break
    if Computer_Chance==0:
        myarray[0,0]=computer_choose
        numbers.remove(Computer_Chance)
        A=(Wincondition())
        if A:
            print("Computer  Win :( ")
            break
    if Computer_Chance==1:
        myarray[0,1]=computer_choose
        numbers.remove(Computer_Chance)
        A=(Wincondition())
        if A:
            print("Computer  Win :( ")
            break
    if Computer_Chance==2:
        myarray[0,2]=computer_choose
        numbers.remove(Computer_Chance)
        A=(Wincondition())
        if A:
            print("Computer  Win :( ")
            break
    if Computer_Chance==3:
        myarray[1,0]=computer_choose
        numbers.remove(Computer_Chance)
        A=(Wincondition())
        if A:
            print("Computer  Win :( ")
            break
    if Computer_Chance==4:
        myarray[1,1]=computer_choose
        numbers.remove(Computer_Chance)
        A=(Wincondition())
        if A:
            print("Computer  Win :( ")
            break
    if Computer_Chance==5:
        myarray[1,2]=computer_choose
        numbers.remove(Computer_Chance)
        A=(Wincondition())
        if A:
            print("Computer  Win :( ")
            break
    if Computer_Chance==6:
        myarray[2,0]=computer_choose
        numbers.remove(Computer_Chance)
        A=(Wincondition())
        if A:
            print("Computer  Win :( ")
            break
    if Computer_Chance==7:
        myarray[2,1]=computer_choose
        numbers.remove(Computer_Chance)
        A=(Wincondition())
        if A:
            print("Computer  Win :( ")
            break
    if Computer_Chance==0:
        myarray[2,2]=computer_choose
        numbers.remove(Computer_Chance)
        A=(Wincondition())
        if A:
            print("Computer  Win :( ")
            break
    if len(numbers)==0:
        break 