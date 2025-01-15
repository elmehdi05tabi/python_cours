 # ----------------------------------------------------------------------------------------
# -- built in functions => reduce 
# ---------------------------------------
# [1] Reduce Take A function + Iterator 
# [2] Reduce Run a fucntion on first and seconde elemnt and give result 
# [3] then run function on result and third elment 
# [4] then run function on result and fourth elment ans so on
# [5] till one elment is left and thsi is the result of the reduce 
# [6] the function ca, be pre-defined function or lambda function 
# ----------------------------------------------------------------------------------------
#  Example 1
from functools import reduce
def sumall(num1,num2)  :
    return num1+num2 
numbers = [10 ,15,20,30,7]
result = reduce(sumall , numbers)
print(result)
# ((((10+15) + 20 )+30)+7)
#  Example 2 
print("#"*50)
from functools import reduce
numbs = [20 , 5 , 6 ,100 ,3 ]
print(reduce(lambda n1,n2 : n1+n2 , numbs))

