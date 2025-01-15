# Loop Advanced Dictionary


mysikill = {
    "foot" : "90%",
    "fransh" : "60%",
    "english":"50%",
    "css" : "80%" 
}

# print(mysikill.items())

for  skill_key , skill_value in mysikill.items() :
   print(f"progres of {skill_key} => {skill_value}")

print ("="*50)

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

for skill_key , skill_value in peaple.items() : 
   print(f"skills of {skill_key.upper()} is : ")
   for child_key , child_value in skill_value.items() :
      print(f"{child_key} => {child_value}")