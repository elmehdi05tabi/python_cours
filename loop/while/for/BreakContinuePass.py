# -----------------------
# ------- for => loop -------
#  break continu bast 
#-------------------------

mylist = [1,2,3,4,5,6,7,8,9]
#  continue 
for i in mylist : 
    if i == 3 :
        continue 
    print(i)
#  break 
print("="*50)
for i in mylist : 
    if i == 3 :
        break 
    print(i)
# pass
print("="*50)
for i in mylist : 
    if i == 3 :
        pass 
    print(i)