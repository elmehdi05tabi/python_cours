# ----------------------------------------------------
# -- Regular Expressions => Re Module Split And Sub --
# ----------------------------------------------------
# split(Pattern, String, MaxSplit)  => Return A List Of Elements Splitted On Each Match
# sub(Pattern, Replace, String, ReplaceCount) => Replace Matches With What You Want
# ---------------------------------------------------------------------
import re 
#* split()
# !----------------------------------------------------------
string_one = "elmehdi tabi rojola"
search_one = re.split(r"\s",string_one,1)
print(search_one)

# for i in range(len(split1)) : 
#     print(f"the {i+1} is {split1[i]}")

print("#"*50) ; 
string_two = "how-to-write_a_very-good-article"
search_two = re.split(r"-|_",string_two)
print(search_two)

print("#"*50) ; 

for counet,word in enumerate(search_two,1) : 
    if len(word)>1 : 
     print(f"word Number : {counet}=> {word.lower()}")
# !---------------------------------------------------------
#^ sub() 
print(re.sub(r"\s","-","I Love Pythone",1))


