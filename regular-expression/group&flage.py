# # -------------------------------------------------------------
# --- Reguler Expressions => Characters Classes Training 
# ------------------------------------

import re 
my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"

search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)",my_web)
print(search.group())
print(search.groups())

for i in search.groups() : 
    print(i)

print("#"*50)
print(f"Protocol : {search.group(1)}")
print(f"Sub Demain : {search.group(1)}")
print(f"Demain Name : {search.group(1)}")
print(f"Top Level Domain  : {search.group(1)}")
print(f"Port : {search.group(1)}")
print(f"Query string : {search.group(1)}")