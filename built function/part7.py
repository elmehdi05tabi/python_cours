# -----------------------------------
# -- Built in Function--
# -----------------------------------
# enumerate()
# help()
# reverse ()
# ----------------------------------
# enumerate(iterable , star => 0) 
mysklls = ["html","css","js","php"]
mySkillWithCounter  = enumerate(mysklls , 20 )
print(type(mySkillWithCounter))
for c,s in mySkillWithCounter : 
    print(f"{c}=>{s}")

print("#"*50)
# help() => help you if you don't undersante any function in python 

print(help(print))

print("#"*50)
# reversed(iterable) 
mystirg = "Elmehdi" 
for i in reversed(mystirg) : 
    print(i)

print("#"*50)
# reversed(iterable) 
mystirg = ["Elmehdi","Tabi","Rajawi","Zad","FiHbalo"] 
for i in reversed(mystirg) : 
    print(i)