# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ---

# the teries you have 
tries = 3 
password = input("select your password").strip().lower()

inputpassword = input("whrit the password :").strip().lower()
while password != inputpassword : 
    tries -= 1 
    print(f"wrong password you have  {"the last tries " if tries==0 else tries} tries")
    inputpassword = input("whrit the password :").strip().lower()
     
    if tries == 0 :
        print("the tries is finished")
        break 
        print(" will not print ")
else : 
    print("the password is trues")