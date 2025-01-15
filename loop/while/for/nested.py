#  -------------------
# ===== loop => for 
# ==== Nested loop ==
#  -------------------

# peaple = ["elmehdi","ahmed","hassn","ali"]
# skill = ["html","css","js"]

# for i in  range( len(skill)) : 
#     print(f"{peaple[i]} skill is {skill[i]} ")


#  dict 


peaple = {
    "elmehdi":{
        "html" :"90%",
        "css" : "25%",
        "python" :"100%"
    },
    "saad":{
          "html" :"20%",
        "css" : "90%",
        "python" :"30%"
    },
    "amine":{
          "html" :"27%",
        "css" : "75%",
        "python" :"70%"
    }
}

for name in peaple : 
    print(f"skill  and progrese for {name}")
    for skill in peaple[name] :
        print(f"{skill} => {peaple[name][skill]}") 
