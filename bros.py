#THKS TO BRILLIANT
import random, time #PLAY RAMDOM WHO CARE =)))
#----_Varible-----
def logintest():
	username = input("username :")
	password = input("passworld:")
	if username == password:
		print("TEST FAIL: bro...Who make password and username duplicate")
	else:
			print("TEST OK")
def loguptest():
		nw_username = input("username:")
		nw_password = input("passoword:")
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

    start_time = time.time()   # thời điểm tạo code
    limit = 30                 # 30 giây

    code = input("enter reset code: ")

    current_time = time.time()

    if current_time - start_time > limit:
        print("TEST FAIL: you make waste of time, now GET OUT!!!!!!")
        return

    if code == reset_code:
        new_pws = input("enter new password: ")
        confirm_pws = input("confirm your password: ")

        if confirm_pws == new_pws:
            print("TEST OK")
        else:
            print("TEST FAIL: password doesn't match")
    else:
        print("TEST FAIL: code doesn't match")
def info():
	print("""I add Borlean on this code fr
but I can be use without .txt
Be for real. Learn → information of file(you will confued what i say)
sorry but i is vietnamese so my gramar will be made you scold at me and yourself =) """)
def myfault():
	print ("Nothing (SO MUCH CHATGPT!!) ")
def some_fun():
	print("what kind of fun are you today?")
	awnser = input("=>")
	if awnser == "9008":
		print("oh no! my phone is Qualcomm =(")
	elif awnser == "main":
		print("ok, but tomorrow is not your main")
#         main
print("""$$$$$$$$$$$$$$$$$$$$$$$$$$$
-------Python Bros---------
$$$$$$$$$$$$$$$$$$$$$$$$$$$
       choose mode
	1.Login
	2.Log up
	3.Reset passworld
	4.information
	5:My fault of programing this
	6:Some kind of fun (beta)
	exit() quit...for now
Update will be soon (1.3)""")
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
	elif key == "exit()":
		print("bye...for now")	
		break
	else:
		print("The code does nothing")