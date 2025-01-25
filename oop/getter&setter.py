# ---------------------------------------------------------------
# -- object oriented programming => Getter&Setter
# ---------------------------------------------------------------

class Member : 
    def __init__(self,name) : 
        self.__name = name 
    def say_hello(self) :
        return f"hello {self.__name}"
    # ! getter => afficher le nom 
    def get_name (self) : 
        return self.__name 
    # ~ setter => modifer le nome 
    def set_name (self,new_nam) : 
        self.__name =  new_nam
        return new_nam
    
one =Member("elmehdi") 
# one._Member__name = "tabi"
# print(one._Member__name) 

print(one.get_name())
print(one.set_name("tabi"))