from utils.classes.grammar import Grammar
from utils.classes.production import Production
from utils.first import first
from utils.follow import follow

grammar = Grammar(
    [
        Production("expression'", "expression"),
        Production("expression", "expression PLUS term"),
        Production("expression", "term"),
        Production("term", "term TIMES factor"),
        Production("term", "factor"),
        Production("factor", "LPAREN expression RPAREN"),
        Production("factor", "ID"),
    ],
    ["PLUS", "TIMES", "LPAREN", "RPAREN", "ID"],
    ["expression", "term", "factor"]
)

print(follow(grammar, "factor"))
