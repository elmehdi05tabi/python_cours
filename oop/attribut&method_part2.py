# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------


class Member : 
    def __init__(self,firt_name,middle_nam,last_name,gender) : 
        self.fname = firt_name
        self.mname = middle_nam
        self.lname = last_name
        self.gender =gender
    def full_name(self) :
        return f"{self.fname} {self.mname} {self.lname}" 
    def name_with_title(self) : 
        if self.gender == "male"  : 
          return f"bonjour Ms {self.fname}"
        elif self.gender == "femmal" : 
            return f"bonjour Md {self.fname}"
        else : 
            return f"bonjour {self.fname}"
    def get_all_info(self) : 
        return f"{self.name_with_title()} Votre nom complet est {self.full_name()}"
member_one = Member("elmehdi","tabi","mahmod","male")
member_two = Member("tabi","hassan","ibrahim","kafir")
member_three = Member("asmae","ossama","essayed","femmal")
# print(dir(member_one))

# print(member_one.full_name())
# print(member_two.full_name())

# print(member_one.full_name())
# print(member_one.name_with_title())
# print(member_two.name_with_title())
# print(member_three.name_with_title())

print(member_one.get_all_info())
print(member_two.get_all_info() )
print(member_three.get_all_info())
