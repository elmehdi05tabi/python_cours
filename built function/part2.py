# -----------------------------
# --- built in function---
# -----------------------------
# sum()
# round()
# range()
# print()
# -----------------------------

# sum(iterable , start)
a = [10 ,20,30,40]
print(sum(a,50))
print("="*50)
# round(number , numofdegits) 
print(round(10.556))
print(round(10.554,2))
print("="*50)
#  range(start,end ,step)
print(list(range(0)))
print(list(range(1,10)))
print(list(range(1,10,2)))

print("="*50)
# print() => sep => default value is space 
print("hello @elmehdi @tabi @how @are @you @today ")
print("hello","elmehdi","tabi","how","are","you","today",sep="|")
print("="*50)
# print() => end() => default value is \n 
print("the first line",end="this is crayzi man")
print("the second line")
print("the last line")