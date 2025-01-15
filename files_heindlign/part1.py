# ------------------------------------------------
# -- file heandlign -- 
# --------------------
# "a"  append  open file for appending values , create file if note exists
# "r"  read    [default value] open file for read and give error if is not exists
#  "w" write open file for writing , create file if not exists 
#  "x" crete file , give error if file exits 
# ------------------------------------------------
# file = open("file","mode(a,r,w,x)")
# [
# we have two type in past  : 
# absolute past => he start in root at the file 
# relative past => relation in your oplace now 
# ] 


# absolute past : 
# file = open(r"C:\Users\tabi\Desktop\python\files_heindlign\elmehdi.txt")

#  relative past  :
#  
import os  # os => operating systeme : 


 # main current working directory : 
# print(os.getcwd()) 

#  change directory : 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

file = open("elmehdi.txt")

# directory for the opened file
#   
# print(os.path.dirname(os.path.abspath(__file__)))

# print(os.path.abspath(__file__)) #=> return  an absolute path : 