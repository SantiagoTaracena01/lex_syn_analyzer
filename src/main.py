from utils.postfix import regex_infix_to_postfix
from utils.thompson import thompson_construction
from utils.show_fa import show_nfa

regex = input("Please, input a regex: ")
postfix = regex_infix_to_postfix(regex)
nfa = thompson_construction(postfix)
show_nfa(nfa)
print(nfa)
