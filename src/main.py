from utils.postfix import regex_infix_to_postfix
from thompson import thompson_construction

regex = input("Please, input a regex: ")
postfix = regex_infix_to_postfix(regex)
nfa = thompson_construction(postfix)
print(nfa)
