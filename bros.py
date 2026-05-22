#THKS TO BRILLIANT
import random
import os
import time
import subprocess #PLAY RAMDOM WHO CARE =)))
#-----Variable-----
Coin = 0
user_subscription = "Free"
def Subscription_Package():
    global Coin
    try:
        print("you have", Coin, "coins and you are",user_subscription,"stage")
        package = int(input("""Enter the subscription package (1, 2, or 3): 
                            1. Basic     - 10 coins   
                            2. Standard  - 20 coins
                            3. Premium   - 30 coins
                            Your choice: """))
        if package == 1:
            cost = 10
        elif package == 2:
            cost = 20
        elif package == 3:
            cost = 30
        else:
            print("Invalid package. Please enter 1, 2, or 3.")
            return Subscription_Package()

        # Check and subtract coins
        if Coin >= cost:
            Coin -= cost
            user_subscription = ["Free", "Basic", "Standard", "Premium"][package]
            print(f"Subscription purchased for {cost} coins. Remaining coins: {Coin}")
            return cost
        else:
            print(f"Not enough coins. You have {Coin}, but need {cost}.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return Subscription_Package()
    except KeyboardInterrupt:
        print("\nSubscription process interrupted. Returning to main menu.")
        return

def clear():
    if os.name == "nt":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run(["clear"])

def load_users():
    users = {}
    try:
        with open("users.txt", "r") as f:
            for line in f:
                u, p = line.strip().split(":")
                users[u] = p
    except FileNotFoundError:
        pass
    return users

def save_user(username, password):
    with open("users.txt", "a") as f:
        f.write(username + ":" + password + "\n")

def logintest():
    users = load_users()

    username = input("username: ")
    password = input("password: ")

    if username in users and users[username] == password:
        print("welcome back bro ")
    else:
        print("GET OUT ")

def loguptest():
    
    nw_username = input("username:")
    nw_password = input("password:")

    if len(nw_password) < 5:
        print("opps, not strong enough ")
    elif nw_username == nw_password:
        print("bro... username = password,just be strong can be hacker ")
    else:
        save_user(nw_username, nw_password)
        print("welcome bro ")

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
    print("""What's New in Python Bros:
    - Improved user authentication system
    - Enhanced subscription management(collect conin by useing all temple. you can be free cause all are same features, like a temple)
    - Bug fixes and performance improvements""")

def myfault():
    print("Nothing in this code is SYTAX ERROR, but there are some logic error, and i will fix it in the future update, but for now, just enjoy this code bro")

def some_fun():
    print("what kind of fun are you today?")
    answer = input("=>")
    if answer == "9008":
        print("oh no! my phone is Qualcomm =(")
    elif answer == "main":
        print("ok, but tomorrow is not your main")
    else:
        print("hey! this joke is fun bro")
#         main
print("you have", Coin, "coins and you are",user_subscription,"stage")
print("""-------Python Bros---------
WERE YOU CAN TAKE A PART OF MY CODE, NON-COPYRIGHT (SOVIET aura)
      $$$$$$$$$$$$$$$$$$$$$$$$$$$
       choose mode
    1.Login (Temple)
    2.Log up (Temple)
    3.Reset passworld (Temple)
    4.what's new?
    5:My fault of programing this
    6:Some kind of fun (beta)
    7:Subscription Package (beta and temple)
    clear():clear all this (remember this 'help')
    exit() quit...for now
Update will be soon (UPDATE DATE: 2026 - 5 - 22/  UPDATE CODE: 3.8.0)""")
try:
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

        elif key == "7":
            Subscription_Package()

        elif key == "clear()":
            clear()

        elif key == "exit()":
            print("bye...for now")
            break

        elif key == "exit" or key == "clear":
            print("just for real, add some ')' pls")

        else:
            print("The code does nothing")

except KeyboardInterrupt:
    print("\nDid you combo Ctrl + C??? Nevermind, bye!")

