# ------------------------------------------
# --  Doc String & Commenting Vs Documenting 
# ------------------------------------------
#  [1] Documentation String For Class ,Module or Funtion
#  [2] Can be accssed from the help and doc attriutes
#  [3] made for undestainding the functionality of the comples  
#  [4] theres one line and multiple line doc strings 
# ------------------------------------------
def elmehdi_func(name) :
    """
    elmehdi function 
      it say hello from elmedhi 
    paremeter : 
     name => persone name tha use fucntion 
     Return  : 
     return name the fucntion  
    """
    print(f"hello {name} from elmehdi")
# elmehdi_func("ahmed")
# print(dir(elmehdi_func))
# print(elmehdi_func.__doc__)
help(elmehdi_func)