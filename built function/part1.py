# -----------------------------
# --- built in function---
# -----------------------------
# all()
# any()
# bin()
# id()
# -----------------------------

# ====================================================
#  all()

# x= [1,2,3,4,]
# if all(x):
#     print("All Elment Is True : ")
# else : 
#     print("Therese Att Least One elments is false :")
# ====================================================
# any()
x= [[],"",{},1]
if any(x):
    print("ther's at least one elments is true : ")
else : 
    print("all elments is false  :")
# ====================================================
# bin() => binary number => the campture languge   :
print(bin(101))
# ====================================================
print("="*50)
# id () 
a=2
b=1
print((f"the id of {a} in the memory is : {id(a)}"))
print((f"the id of {b} in the memory is : {id(b)}"))