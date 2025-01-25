# --------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
# --------------------------------------------------
# Encapsulation
# - Restrict Access To The Data Stored in Attirbutes and Methods
# Public
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside Our Outside The Class
# Protected
# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore _
# Private
# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __
# ---------------------------------------------------------
# - Attributes = Variables = Properties
# -------------------------------------
# ! Puplic 
class Member1 : 
    def __init__(self,name) : 
        self.name = name 
one =  Member1("elmehdi")
# print(one.name)
# one.name = "tabi"
# print(one.name)


#& Proected 
class Member2 : 
    def __init__(self,name) : 
        self._name = name 
one =  Member2("elmehdi")
print(one._name)

#^ Privat 
class Member3 : 
    def __init__(self,name) : 
        self.__name = name 
    def say_hello (self) : 
        return f"hello {self.__name}"
one =  Member3("elmehdi")
# print(one.__name)
print(one.say_hello())
print(one._Member3__name)
