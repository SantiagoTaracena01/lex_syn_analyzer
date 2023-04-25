import sys
from utils.direct_construction import direct_construction
from utils.simulate_yalex_file import simulate_yalex_file

dfa = direct_construction(
    ['32', '9', '|', '10', '|', '+', '#0', '.', '65', '66', '|', '67', '|', '68', '|', '69', '|', '70', '|', '71', '|', '72', '|', '73', '|', '74', '|', '75', '|', '76', '|', '77', '|', '78', '|', '79', '|', '80', '|', '81', '|', '82', '|', '83', '|', '84', '|', '85', '|', '86', '|', '87', '|', '88', '|', '89', '|', '90', '|', '97', '|', '98', '|', '99', '|', '100', '|', '101', '|', '102', '|', '103', '|', '104', '|', '105', '|', '106', '|', '107', '|', '108', '|', '109', '|', '110', '|', '111', '|', '112', '|', '113', '|', '114', '|', '115', '|', '116', '|', '117', '|', '118', '|', '119', '|', '120', '|', '121', '|', '122', '|', '65', '66', '|', '67', '|', '68', '|', '69', '|', '70', '|', '71', '|', '72', '|', '73', '|', '74', '|', '75', '|', '76', '|', '77', '|', '78', '|', '79', '|', '80', '|', '81', '|', '82', '|', '83', '|', '84', '|', '85', '|', '86', '|', '87', '|', '88', '|', '89', '|', '90', '|', '97', '|', '98', '|', '99', '|', '100', '|', '101', '|', '102', '|', '103', '|', '104', '|', '105', '|', '106', '|', '107', '|', '108', '|', '109', '|', '110', '|', '111', '|', '112', '|', '113', '|', '114', '|', '115', '|', '116', '|', '117', '|', '118', '|', '119', '|', '120', '|', '121', '|', '122', '|', '95', '*', '|', '48', '49', '|', '50', '|', '51', '|', '52', '|', '53', '|', '54', '|', '55', '|', '56', '|', '57', '|', '|', '*', '.', '#1', '.', '|', '48', '49', '|', '50', '|', '51', '|', '52', '|', '53', '|', '54', '|', '55', '|', '56', '|', '57', '|', '+', '46', '48', '49', '|', '50', '|', '51', '|', '52', '|', '53', '|', '54', '|', '55', '|', '56', '|', '57', '|', '+', '.', '?', '.', '69', '43', '45', '|', '?', '.', '48', '49', '|', '50', '|', '51', '|', '52', '|', '53', '|', '54', '|', '55', '|', '56', '|', '57', '|', '+', '.', '?', '.', '#2', '.', '|', '59', '#3', '.', '|', '58', '61', '.', '#4', '.', '|', '60', '#5', '.', '|', '61', '#6', '.', '|', '43', '#7', '.', '|', '45', '#8', '.', '|', '42', '#9', '.', '|', '47', '#10', '.', '|', '40', '#11', '.', '|', '41', '#12', '.', '|', '35', '.'],
    [('return WHITESPACE', 'WHITESPACE'), ('return ID', 'ID'), ('return NUMBER', 'NUMBER'), ('return SEMICOLON', 'SEMICOLON'), ('return ASSIGNOP', 'ASSIGNOP'), ('return LT', 'LT'), ('return EQ', 'EQ'), ('return PLUS', 'PLUS'), ('return MINUS', 'MINUS'), ('return TIMES', 'TIMES'), ('return DIV', 'DIV'), ('return LPAREN', 'LPAREN'), ('return RPAREN', 'RPAREN')]
)

test_file = sys.argv[1] if (len(sys.argv) > 1) else "./tests/slr-1-test.txt"

def return_token(found_token):

    WHITESPACE = "WHITESPACE"
    ID = "ID"
    NUMBER = "NUMBER"
    SEMICOLON = "SEMICOLON"
    ASSIGNOP = "ASSIGNOP"
    LT = "LT"
    EQ = "EQ"
    PLUS = "PLUS"
    MINUS = "MINUS"
    TIMES = "TIMES"
    DIV = "DIV"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"

    if (found_token == WHITESPACE):
        return WHITESPACE
    if (found_token == ID):
        return ID
    if (found_token == NUMBER):
        return NUMBER
    if (found_token == SEMICOLON):
        return SEMICOLON
    if (found_token == ASSIGNOP):
        return ASSIGNOP
    if (found_token == LT):
        return LT
    if (found_token == EQ):
        return EQ
    if (found_token == PLUS):
        return PLUS
    if (found_token == MINUS):
        return MINUS
    if (found_token == TIMES):
        return TIMES
    if (found_token == DIV):
        return DIV
    if (found_token == LPAREN):
        return LPAREN
    if (found_token == RPAREN):
        return RPAREN

simulate_yalex_file(test_file, dfa, return_token)
