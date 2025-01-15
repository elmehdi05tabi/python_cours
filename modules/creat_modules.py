# ------------------------------------------------
# -- Modules => Creat Your Module -- 
# ------------------------------------------------
# pour crée vous modules la premier chose c'est crée vous ficher pour stocker le modules 
# import sys 
# sys.path.append(r"D:\Games")
# print(sys.path)
# import elmehdi 
# # print(dir(elmehdi))
# name=input("entre le nom :").capitalize().strip()
# elmehdi.say_hello(name)
# elmehdi.say_how_areyou(name)


#    Alia import  اسم مستعار  


# import elmehdi  as el 
# # print(dir(elmehdi))
# name=input("entre le nom :").capitalize().strip()
# el.say_hello(name)
# el.say_how_areyou(name)

# alias for import fucntion : 

from elmehdi import say_how_areyou as sh 
sh("elmehdi")