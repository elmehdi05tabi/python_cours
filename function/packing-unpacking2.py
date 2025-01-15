# -------------------------------------- -------------
# -- function packing , unpacking argumnets **kwArgs ----
# -------------------------------------- -------------

# def sho_skills(*skills) :
#     print(type(skills))
#     for skill in skills : 
#         print(f"{skill}")
# sho_skills("html","css","js","p")
mys = {
    "html":"90%" ,
     "css" : "50%", 
     "js" :"50%",
     "python":"80%"
    }

def sho_skills(**skills) :
    print(type(skills))
    for skill,value in skills.items() : 
        print(f"{skill} => {value}")

sho_skills(**mys)