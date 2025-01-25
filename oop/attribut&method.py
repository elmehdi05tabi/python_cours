# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------


class Member : 
    def __init__(self,firt_name,middle_nam,last_name) : 
        self.fname = firt_name
        self.mname = middle_nam
        self.lname = last_name
member_one = Member("elmehdi","tabi","mahmod")
member_two = Member("tabi","hassan","ibrahim")
member_three = Member("ahmed","ossama","essayed")
# print(dir(member_one))

print(member_one.fname,member_one.mname,member_one.lname)
print(member_two.fname)
print(member_three.fname)