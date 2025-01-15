# ===================
# =====  Methods Part One =====
# ===================

# clear

user ={
    "name":"elmehdi"
}
user.clear()
print(user)

print("="*50)

# update => ajecter un elment en dict

user ={
    "name":"elmehdi"
}
# method 1
user['age']="19 ans"
print(user)
# method 2
user1 ={
    "name":"elmehdi"
}
user1.update({"count":"morocco","city":"settet"})
print(user1)
print("="*50)
#  copy 
main ={
    "name" : "elmehdi"
}
b = main.copy()
print(main)
print(b)
main.update({"deplome":"ts"})
print(main)
print(b)