import sys
from utils.direct_construction import direct_construction
from utils.simulate_yalex_file import simulate_yalex_file

dfa = direct_construction(
    ['32', '9', '|', '10', '|', '+', '#0', '.', '37', '116', '.', '111', '.', '107', '.', '101', '.', '110', '.', '#1', '.', '|', '73', '71', '.', '78', '.', '79', '.', '82', '.', '69', '.', '#2', '.', '|', '47', '42', '.', '#3', '.', '|', '42', '47', '.', '#4', '.', '|', '37', '37', '.', '#5', '.', '|', '43', '42', '.', '45', '47', '.', '|', '#6', '.', '|', '65', '66', '|', '67', '|', '68', '|', '69', '|', '70', '|', '71', '|', '72', '|', '73', '|', '74', '|', '75', '|', '76', '|', '77', '|', '78', '|', '79', '|', '80', '|', '81', '|', '82', '|', '83', '|', '84', '|', '85', '|', '86', '|', '87', '|', '88', '|', '89', '|', '90', '|', '*', '#7', '.', '|', '97', '98', '|', '99', '|', '100', '|', '101', '|', '102', '|', '103', '|', '104', '|', '105', '|', '106', '|', '107', '|', '108', '|', '109', '|', '110', '|', '111', '|', '112', '|', '113', '|', '114', '|', '115', '|', '116', '|', '117', '|', '118', '|', '119', '|', '120', '|', '121', '|', '122', '|', '*', '#8', '.', '|', '37', '#9', '.', '|', '58', '#10', '.', '|', '59', '#11', '.', '|', '124', '#12', '.', '|', '35', '.'],
    [('return WHITESPACE', 'WHITESPACE'), ('return TOKEN', 'TOKEN'), ('return IGNORE', 'IGNORE'), ('return LEFTCOMMENT', 'LEFTCOMMENT'), ('return RIGHTCOMMENT', 'RIGHTCOMMENT'), ('return SPLIT', 'SPLIT'), ('return CHARACTERS', 'CHARACTERS'), ('return TERMINAL', 'TERMINAL'), ('return NONTERMINAL', 'NONTERMINAL'), ('return PERCENTAGE', 'PERCENTAGE'), ('return COLON', 'COLON'), ('return SEMICOLON', 'SEMICOLON'), ('return OR', 'OR')]
)

test_file = sys.argv[1] if (len(sys.argv) > 1) else "./tests/slr-1-test.txt"
output_file = sys.argv[2] if (len(sys.argv) > 2) else "./out/output.txt"
output_type = sys.argv[3] if (len(sys.argv) > 3) else "analysis"

def return_token(found_token):

    WHITESPACE = "WHITESPACE"
    TOKEN = "TOKEN"
    IGNORE = "IGNORE"
    LEFTCOMMENT = "LEFTCOMMENT"
    RIGHTCOMMENT = "RIGHTCOMMENT"
    SPLIT = "SPLIT"
    CHARACTERS = "CHARACTERS"
    TERMINAL = "TERMINAL"
    NONTERMINAL = "NONTERMINAL"
    PERCENTAGE = "PERCENTAGE"
    COLON = "COLON"
    SEMICOLON = "SEMICOLON"
    OR = "OR"

    if (found_token == WHITESPACE):
        return WHITESPACE
    if (found_token == TOKEN):
        return TOKEN
    if (found_token == IGNORE):
        return IGNORE
    if (found_token == LEFTCOMMENT):
        return LEFTCOMMENT
    if (found_token == RIGHTCOMMENT):
        return RIGHTCOMMENT
    if (found_token == SPLIT):
        return SPLIT
    if (found_token == CHARACTERS):
        return CHARACTERS
    if (found_token == TERMINAL):
        return TERMINAL
    if (found_token == NONTERMINAL):
        return NONTERMINAL
    if (found_token == PERCENTAGE):
        return PERCENTAGE
    if (found_token == COLON):
        return COLON
    if (found_token == SEMICOLON):
        return SEMICOLON
    if (found_token == OR):
        return OR

simulate_yalex_file(test_file, output_file, dfa, output_type, return_token)
