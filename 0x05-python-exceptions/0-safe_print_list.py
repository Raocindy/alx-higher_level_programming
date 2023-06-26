#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    balls = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            balls += 1
        except IndexError:
            break
    print()
    return(balls)
