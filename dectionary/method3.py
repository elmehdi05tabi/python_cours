# ===================
# =====  Methods Part One =====
# ===================


# setdefault => si il y a le key il est affiche le key 
#  sinon il est faire update 

user={
    "name":"elmehdi"
}
print(user)
print(user.setdefault("name","elzero"))
print(user)
print(user.setdefault("name1","elzero"))
print(user)
print("="*50)
# popitem()=> il ma donne la dernier elment qui est ajoute 
membre = {
    "name" :"elmehdi",
    "name2":"tabi"
}
membre["age"]=19
print(membre.popitem())

# items() => giv all items in dect 
print("="*50)

membre = {
    "name" :"elmehdi",
    "name2":"tabi"
}
allitems=membre.items()
print(allitems)
print("="*50)
# formkeys=> creat in dictionary 
a=("key1","key2","key3")
b='1'
print(dict.fromkeys(a,b))