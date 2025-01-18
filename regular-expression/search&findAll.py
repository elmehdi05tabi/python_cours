# -------------------------------------------------------------
# --- Reguler Expressions => Characters Classes Training 
# -------------------------------------------------------------
# Search() => serach a string for a match and return a first match only
# findall() => retutns a list of all matches and empty list if no match 
# -------------------------------------------------------------
# Email Pattern => # ^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)$
# -------------------------------------------------------------
import re 
# ^  search ()
# my_string  = re.search(r"[A-Z]{2}","EElmehdiTTabi")
# print(my_string)
# print(my_string.span())
# print(my_string.string)

# ! exeample pour teste le email : 
# is_email = re.search(r"^[A-z0-9\.]+@[A-z0-9]+\.(com|net)$","elemhdi@gmail.com")
# if is_email : 
#     print("c'est une email")
#     print(is_email.span())
#     print(is_email.string)
#     print(is_email.group())
# else : 
#     print("c'est pas email")

# ^  findall ()


email = input("entre votre email") 
search = re.findall("^[A-z0-9\.]+@[A-z0-9]+\.(com|net)$",email)
list_email = []
if search!=[] : 
    list_email.append(email)
    print("email ajouter")
else : 
    print("invalid email")
for i in list_email : 
    print(i)
