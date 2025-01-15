# --------------------------------------------------------
#  -- finction packing , unpaking argument trainings -- 
# --------------------------------------------------------
skill=("html","css","js")
skillprogrs = {
    "sql":"90%",
    "go" :"20%",
    "ts" : "80%"
}
def show_skills(name,*skill,**skillprogress):
    print(f"hello {name} \nthis is your skill without progress")
    for skills in skill :
        print(skills.upper())
    print("this is skill with progress :")
    for skill_key ,skill_value in skillprogress.items() : 
        print(f"{skill_key.upper()} the progress is : {skill_value}")

show_skills("osama",*skill,**skillprogrs)