# -------------------------------------------------------------------
# -- Object Oriented Programming => Class Methods & Static Methods --
# -------------------------------------------------------------------
# Class Methods:
# - Marked With @classmethod Decorator To Flag It As Class Method
# - It Take Cls Parameter Not Self To Point To The Class not The Instance
# - It Doesn't Require Creation of a Class Instance
# - Used When You Want To Do Something With The Class Itself
# Static Methods:
# - It Takes No Parameters
# - Its Bound To The Class Not Instance
# - Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class
# -----------------------------------------------------------

class Member : 
    @classmethod 
    def shos_user_count (cls) : 
         return f"le nombre des utilisators est : {Member.user_nama}"
    @staticmethod 
    def say_hello () : 
         return "hello from static method"
    user_nama = 0
    def __init__ (self,first_name,middl_name,last_name,genre) :
        self.fname = first_name 
        self.dname = middl_name 
        self.lname = last_name 
        self.genre = genre
        Member.user_nama+=1
    def full_name (self) :
            return f"{self.fname} {self.dname} {self.lname}"
    def name_with_title (self) : 
        if self.genre == "Homme" : 
            return f"salut monsseiure {self.fname}"
        elif self.genre ==  "Famme" : 
            return f"salut madame {self.fname}"
        else :
            return f"salut {self.fname}"
    def gitt_all_info (self)  : 
          return f"{self.name_with_title()} , vous nom complet est : {self.full_name()}"
    def delet_user (self) : 
        Member.user_nama -=1
        return f"{self.fname} est suprimer"
print(Member.user_nama)
membre_one = Member("elmehdi","tabi","mjid","Homme")
membre_two = Member ("asmea","tabi","brahim","Famme")
membre_three = Member("hassan","bja3d","howa","homme")
membre_four = Member ("shit","bro","what","go")
print(Member.user_nama)
membre_four.delet_user()
print(Member.user_nama)
print(membre_one.gitt_all_info())
print(membre_two.gitt_all_info())
print(membre_three.gitt_all_info())
print(Member.shos_user_count())
(Member.say_hello())
print("#"*50)
print(membre_one.full_name())
print(Member.full_name(membre_one))