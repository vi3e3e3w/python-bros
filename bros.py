#THKS TO BRILLIANT
import random
import os
import time #PLAY RAMDOM WHO CARE =)))
#-----Variable-----
def clear():
    os.system("cls" if os.name == "nt" else "clear")

users = {
    "admin": "admin",
    "tests": "12345"
}

def logintest():
    username = input("username: ")
    password = input("password: ")

    if username in users and users[username] == password:
        print("TEST OK")
    else:
        print("GET OUT, USERNAME NOT IN LIST")

def loguptest():
    nw_username = input("username:")
    nw_password = input("password:")
    limit = 5
    if len(nw_password) < limit:
        print("opps, not strong enough")
    elif nw_username == nw_password:
        print("TEST FAIL: USERNAME ≠ PASSWORD")
    else:
        print("TEST OK")

def reset():
    reset_code = str(random.randint(1000, 9999))
    print("PASTE THE", reset_code, "IN THAT INPUT BRO")

    start_time = time.time()
    limit = 30

    code = input("enter reset code: ")
    current_time = time.time()

    if current_time - start_time > limit:
        print("TEST FAIL: you make waste of time")
        return

    if code == reset_code:
        new_pws = input("enter new password: ")
        confirm_pws = input("confirm your password: ")

        if new_pws == confirm_pws:
            print("TEST OK")
        else:
            print("TEST FAIL: password doesn't match")
    else:
        print("TEST FAIL: code doesn't match")

def info():
    print("""Fix some bugs""")

def myfault():
    print("Nothing (SO MUCH CHATGPT!!) ")

def some_fun():
    print("what kind of fun are you today?")
    answer = input("=>")
    if answer == "9008":
        print("oh no! my phone is Qualcomm =(")
    elif answer == "main":
        print("ok, but tomorrow is not your main")
#         main

print("""-------Python Bros---------
$$$$$$$$$$$$$$$$$$$$$$$$$$$
       choose mode
    1.Login
    2.Log up
    3.Reset passworld
    4.information
    5:My fault of programing this
    6:Some kind of fun (beta)
    clear():clear all this (remember this 'help')
    exit() quit...for now
Update will be soon (UPDATE DATE: 2026-27-4 UPDATE CODE: 2)""")
while True:
    key = input(">>>")
    if key == "1":
        logintest()
    elif key == "2":
        loguptest()
    elif key == "3":
        reset()
    elif key == "4":
        info()
    elif key == "5":
        myfault()
    elif key == "6":
        some_fun()
    elif key == "clear()":
        clear()
    elif key == "exit()":
        print("bye...for now")
        break
    elif key == "exit" and "clear":
        print("just for real, add some ')' pls")
    else:
        print("The code does nothing")
