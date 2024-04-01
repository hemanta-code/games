import random

a=1
b=2
c=3
d=4
e=5
f=6
g=7
h=8
i=9
turn=1
user1=1
user2=2
turn_list=[]
user1_list=[]
user2_list=[]

def enter_Value():
    global a,b,c,d,e,f,g,h,i,turn
    print("1 2 3\n4 5 6\n7 8 9\n")
    while turn<=9:
        if turn%2!=0:
            user1=int(input("User1 Turn => "))
            if user1<=9 and user1>=1:
                if user1==1:
                    a="+"
                elif user1==2:
                    b="+"

                elif user1==3:
                    c="+"
                elif user1==4:
                    d="+"
                elif user1==5:
                    e="+"
                elif user1==6:
                    f="+"
                elif user1==7:
                    g="+"
                elif user1==8:
                    h="+"
                else:
                    i="+"
                turn+=1
                turn_list.append(user1)
                user1_list.append(user1)
            else:
                print("enter valid input")
            print("User1 Entered: ",user1,"\n",a,b,c,"\n",d,e,f,"\n",g,h,i)
            print("Turn list : ",turn_list)
            print("user1 list : ",user1_list)
        else:
            user2=int(input("User2 Turn => "))
            if user2==1:
                a="-"
            elif user2==2:
                b="-"
            elif user2==3:
                c="-"
            elif user2==4:
                d="-"
            elif user2==5:
                e="-"
            elif user2==6:
                f="-"
            elif user2==7:
                g="-"
            elif user2==8:
                h="-"
            else:
                i="-"
            turn+=1
            turn_list.append(user2)
            user2_list.append(user2)
            print("User2 entered: ",user2,"\n",a,b,c,"\n",d,e,f,"\n",g,h,i)
            print("Turn list : ",turn_list)
            print("user2 list : ",user2_list)

def win_list():
    win1=[1,2,3]
    win2=[4,5,6]
    win3=[7,8,9]
    win4=[1,4,7]
    win5=[2,5,8]
    win6=[3,6,9]
    win7=[1,5,9]
    win8=[3,5,7]
    # if user1==win1:
        


enter_Value()