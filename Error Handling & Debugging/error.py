# -----------------------------------
# -- Errors And Exceptions Raising --
# -----------------------------------
# [1] Exceptions Is A Runtime Error Reporting Mechanism
# [2] Exception Gives You The Message To Understand The Problem
# [3] Traceback Gives You The Line To Look For The Code in This Line
# [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
# [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# [6] raise Keyword Used To Raise Your Own Exceptions
# -----------------------------------------------------------------

# x = -10 
# if x < 0 : 
#     raise Exception("s'il vous plait entre un nombre suêrier à  0")
# else : 
#     print(f"{x} est bonne nombre et ok ") 

# print("términer le condition ")

dc = {"elmehdi":10 , 5 : "tabi" , "age" : 20   }
for i in dc.keys() : 
 if type(i)== int : 
    raise KeyError ("nous pas faire des nombre en mot cle")
print("términer le condition ") 