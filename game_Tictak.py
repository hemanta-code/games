# import random

# compTurn= random.randint(1,9)
dict_map={
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9
}

def enter_Value():
    userInput=int(input("Your Turn :\n1 2 3\n4 5 6\n7 8 9\n =>"))
    key_list=list(dict_map.keys())
    val_list=list(dict_map.values())
    get_key=val_list.index(userInput)
    # print(key_list[get_key])
    key_list[get_key]='+'
    print("Your Turn :\n",dict_map['a'],dict_map['b'])
    # if userInput==1:
    #     a="+"
        

enter_Value()