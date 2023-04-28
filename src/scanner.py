import sys
from utils.direct_construction import direct_construction
from utils.simulate_yalex_file import simulate_yalex_file

dfa = direct_construction(
    ['32', '9', '|', '10', '|', '+', '#0', '.', '40', '#1', '.', '|', '41', '#2', '.', '|', '#3', '|', '#4', '|', '108', '101', '.', '116', '.', '#5', '.', '|', '61', '#6', '.', '|', '#7', '|', '#8', '|', '43', '#9', '.', '|', '42', '#10', '.', '|', '63', '#11', '.', '|', '114', '117', '.', '108', '.', '101', '.', '#12', '.', '|', '116', '111', '.', '107', '.', '101', '.', '110', '.', '115', '.', '#13', '.', '|', '65', '66', '|', '67', '|', '68', '|', '69', '|', '70', '|', '71', '|', '72', '|', '73', '|', '74', '|', '75', '|', '76', '|', '77', '|', '78', '|', '79', '|', '80', '|', '81', '|', '82', '|', '83', '|', '84', '|', '85', '|', '86', '|', '87', '|', '88', '|', '89', '|', '90', '|', '97', '|', '98', '|', '99', '|', '100', '|', '101', '|', '102', '|', '103', '|', '104', '|', '105', '|', '106', '|', '107', '|', '108', '|', '109', '|', '110', '|', '111', '|', '112', '|', '113', '|', '114', '|', '115', '|', '116', '|', '117', '|', '118', '|', '119', '|', '120', '|', '121', '|', '122', '|', '65', '66', '|', '67', '|', '68', '|', '69', '|', '70', '|', '71', '|', '72', '|', '73', '|', '74', '|', '75', '|', '76', '|', '77', '|', '78', '|', '79', '|', '80', '|', '81', '|', '82', '|', '83', '|', '84', '|', '85', '|', '86', '|', '87', '|', '88', '|', '89', '|', '90', '|', '97', '|', '98', '|', '99', '|', '100', '|', '101', '|', '102', '|', '103', '|', '104', '|', '105', '|', '106', '|', '107', '|', '108', '|', '109', '|', '110', '|', '111', '|', '112', '|', '113', '|', '114', '|', '115', '|', '116', '|', '117', '|', '118', '|', '119', '|', '120', '|', '121', '|', '122', '|', '95', '*', '|', '48', '49', '|', '50', '|', '51', '|', '52', '|', '53', '|', '54', '|', '55', '|', '56', '|', '57', '|', '|', '*', '.', '#14', '.', '|', '48', '49', '|', '50', '|', '51', '|', '52', '|', '53', '|', '54', '|', '55', '|', '56', '|', '57', '|', '+', '#15', '.', '|', '35', '.'],
    [('return WHITESPACE', 'WHITESPACE'), ('return WHITESPACE', 'WHITESPACE'), ('return LPAREN', 'LPAREN'), ('return RPAREN', 'RPAREN'), ('return LEFTCOMMENT', 'LEFTCOMMENT'), ('return RIGHTCOMMENT', 'RIGHTCOMMENT'), ('return LET', 'LET'), ('return EQ', 'EQ'), ('return OR', 'OR'), ('return POSITIVE', 'POSITIVE'), ('return KLEENE', 'KLEENE'), ('return NULLABLE', 'NULLABLE'), ('return RULE', 'RULE'), ('return TOKENS', 'TOKENS'), ('return WORD', 'WORD'), ('return DIGITS', 'DIGITS')]
)

test_file = sys.argv[1] if (len(sys.argv) > 1) else "./tests/slr-1-test.txt"
output_file = sys.argv[2] if (len(sys.argv) > 2) else "./out/output.txt"

def return_token(found_token):

    WHITESPACE = "WHITESPACE"
    WHITESPACE = "WHITESPACE"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    LEFTCOMMENT = "LEFTCOMMENT"
    RIGHTCOMMENT = "RIGHTCOMMENT"
    LET = "LET"
    EQ = "EQ"
    OR = "OR"
    POSITIVE = "POSITIVE"
    KLEENE = "KLEENE"
    NULLABLE = "NULLABLE"
    RULE = "RULE"
    TOKENS = "TOKENS"
    WORD = "WORD"
    DIGITS = "DIGITS"

    if (found_token == WHITESPACE):
        return WHITESPACE
    if (found_token == WHITESPACE):
        return WHITESPACE
    if (found_token == LPAREN):
        return LPAREN
    if (found_token == RPAREN):
        return RPAREN
    if (found_token == LEFTCOMMENT):
        return LEFTCOMMENT
    if (found_token == RIGHTCOMMENT):
        return RIGHTCOMMENT
    if (found_token == LET):
        return LET
    if (found_token == EQ):
        return EQ
    if (found_token == OR):
        return OR
    if (found_token == POSITIVE):
        return POSITIVE
    if (found_token == KLEENE):
        return KLEENE
    if (found_token == NULLABLE):
        return NULLABLE
    if (found_token == RULE):
        return RULE
    if (found_token == TOKENS):
        return TOKENS
    if (found_token == WORD):
        return WORD
    if (found_token == DIGITS):
        return DIGITS

simulate_yalex_file(test_file, output_file, dfa, return_token)
