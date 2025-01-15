#-----------------------
# strings indexing and slacing
# [1] tout les data en python is object 
# [2] object contain elmenet 
# [3] every elment has its own index 
# [4] python utlise zero base de index (index commence en zero)
# [5] use squre brackets to acces element
# [6] enable accessing parts of stings, tuples or liste 
# -----------------------


# indexing (access single istems ) 

monchaine="elmehdi tabi j'ai 18 ans"
print(monchaine[0])  # print => e
print(monchaine[13]) # print => j
print(monchaine[-3]) # print => a : valeure negative commence en la fin de string 

# slicing 
# [start : end] end not included
# [start : end : step ]
print(monchaine[0:12]) # start in 0 => e  end in 12 => i 
print(monchaine[8:12]) # tabi 
print(monchaine[2:5]) # meh 
print(monchaine[::1]) # elmehdi tabi j'ai 18 ans
print(monchaine[::2]) # emhitb 'i1 n
print(monchaine[2:10:2]) #mhit