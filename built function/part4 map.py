# --------------------------------------------
# -- built in fucntion  => map --
# --------------------------------------------
# [1] map take a function + iterator
# [2] map called map because it map the fucntion on every elments 
# [3] the function can be pre-defined function or lamda function
# --------------------------------------------

#  Use Map white Predifened Function 

def formatText(text) : 
    return f"- {text.strip().capitalize()} -"
mytext = ["elmehdi","tabi","osama"] 

myformatedata = map(formatText , mytext) 
print(myformatedata)  # map object => all data in python is object  => donne le adress dans le memoire 

for i in list(map(formatText , mytext))  : 
    print(i)

#  Use Map white lambda  Function 
print("="*50)

mytext = ["elmehdi","tabi","osama"] 

for i in list(map((lambda text : f"- {text.strip().capitalize()} -") , mytext))  : 
    print(i)
