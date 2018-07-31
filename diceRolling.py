import random
from time import sleep

def roll_d20():
    for x in range(1,5):
        print("-", end = "")
        sleep(0.1)
        print("|", end = "")
        sleep(0.1)
    print("->", end = " ")
    rand_num = random.randint(1,20)
    print(rand_num)
    return rand_num

def roll_d12():
    for x in range(1,5):
        print("-", end = "")
        sleep(0.1)
        print("|", end = "")
        sleep(0.1)
    print("->", end = " ")
    rand_num = random.randint(1,12)
    print(rand_num)
    return rand_num

def roll_d10():
    for x in range(1,5):
        print("-", end = "")
        sleep(0.1)
        print("|", end = "")
        sleep(0.1)
    print("->", end = " ")
    rand_num = random.randint(1,10)
    print(rand_num)
    return rand_num

def roll_d8():
    for x in range(1,5):
        print("-", end = "")
        sleep(0.1)
        print("|", end = "")
        sleep(0.1)
    print("->", end = " ")
    rand_num = random.randint(1,8)
    print(rand_num)
    return rand_num

def roll_d6():
    for x in range(1,5):
        print("-", end = "")
        sleep(0.1)
        print("|", end = "")
        sleep(0.1)
    print("->", end = " ")
    rand_num = random.randint(1,6)
    print(rand_num)
    return rand_num

def roll_d4():
    for x in range(1,5):
        print("-", end = "")
        sleep(0.1)
        print("|", end = "")
        sleep(0.1)
    print("->", end = " ")
    rand_num = random.randint(1,4)
    print(rand_num)
    return rand_num

def roll_d3():
    for x in range(1,5):
        print("-", end = "")
        sleep(0.1)
        print("|", end = "")
        sleep(0.1)
    print("->", end = " ")
    rand_num = random.randint(1,3)
    print(rand_num)
    return rand_num

def roll_d2():
    for x in range(1,5):
        print("-", end = "")
        sleep(0.1)
        print("|", end = "")
        sleep(0.1)
    print("->", end = " ")
    rand_num = random.randint(1,2)
    print(rand_num)
    return rand_num



