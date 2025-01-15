# ---------------------------------------
# ------ Function Recursion ------
# ---------------------------------------
# ------------------------------------------------------------------------------
#  to understand recursion , you need to first undestand recursion
# ------------------------------------------------------------------------------
# word="wwwoooorrrldd" print(word[1:])

def clean_word(word) :
    if len(word) == 1 : 
        return word 
    print(f"print befor start the function {word}")
    if word[0] == word[1] :
        print(f"print before the condition {word}")
        return  clean_word(word[1:])
    print(f"print before retun {word}")
    return word[0] + clean_word(word[1:])

word = input("entre the word :")
print(clean_word(word))