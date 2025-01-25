# # -----------------------------------------------------
# -- Object Oriented Programming => Class Attributes --
# -----------------------------------------------------
# Class Attributes: Attributes Defined Outside The Constructor
# -----------------------------------------------------------

class Member : 
    list_movais_nom = ["shit","ass","4lid"]
    user_nama = 0
    def __init__ (self,first_name,middl_name,last_name,genre) :
        self.fname = first_name 
        self.dname = middl_name 
        self.lname = last_name 
        self.genre = genre
        Member.user_nama+=1
    def full_name (self) :
        if self.fname in Member.list_movais_nom :
            raise ValueError ("ce nom pas valid")
        else :
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
print (membre_four.full_name())