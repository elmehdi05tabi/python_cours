# --------------------------------------------
# -- Modules => Built In Modules 
# --------------------------------------------
#  [1] Modules Is A file contain A set of fucntions
#  [2] You can import modules in your app to help you
#  [3] you can import multiple modules 
#  [4] you can create your own modules
#  [5] modules saves your time 
# --------------------------------------------

# Import main module 
# import random 
# print(random)
# print(f"print random float number {random.random()}")

#  show all function inside modules 

# import random
# print(dir(random))

#  import one or two functions  from module 
from random import randint,random # je peux utilisé le * pour tous les fonction dans cette import 
print(f"Print Random Float {random()}")
print(f"Print Random Intger {randint(100 , 900)}")