# -----------------------
# ------- for => loop -------
#-------------------------
# for item in interable_object : 
    # do something white item 
# -----------------------------------

# item is a variable you creat ans Call Whenever You Want 
# item refer to thr current position and will run ans visit all atems to the end 
# interable_object => sequence [list ,tuples,set,dict,string of characters,ect ...]

mylist = [1,2,3,4,5,6,7,8,9]
for list in mylist : 
    if list % 2 == 0 :
        print(f"this number {list} is even")
    else : 
            print(f"this number {list} is odd")
else : 
     print("for is a finish")

print("="*50)

mys="elmehdi"
for string in mys :
     print(f"{mys.index(string)+1   }[{string}]") 