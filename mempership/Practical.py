admins=[]
for i in range (6):
    admin=input("entre the admin in this group :").strip()
    admins.append(admin)
print(admins)
name=input("entre you name : ")
if name in admins : 
    print(f" hello {name} welcom back  to your group ")
    status = input("you want update you name or delete you name :").strip()
    if status=="update" or status=="u" :
        newname=input("please chois your now name : ").strip()
        admins[admins.index(name)] = newname
        print("name update") 
        print(admins)
    elif status=="delete" or status=="d":
        admins.remove(name)
        print("name delete")
        print(admins)
    else :
        print("sorry this chois indefiend ")
else : 
    status = input(f" hello {name}your not admine, you want add admin , yes or no :")
    if status=="yes" or status=="y" :
        admins.append(name)
        print("your admin now")
        print(admins)
    else :
        print(" your not admin ") 
