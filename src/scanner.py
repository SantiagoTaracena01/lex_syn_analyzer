import sys
from utils.direct_construction import direct_construction
from utils.simulate_yalex_file import simulate_yalex_file

dfa = direct_construction(
    ['32', '9', '|', '10', '|', '+', '#0', '.', '65', '66', '|', '67', '|', '68', '|', '69', '|', '70', '|', '71', '|', '72', '|', '73', '|', '74', '|', '75', '|', '76', '|', '77', '|', '78', '|', '79', '|', '80', '|', '81', '|', '82', '|', '83', '|', '84', '|', '85', '|', '86', '|', '87', '|', '88', '|', '89', '|', '90', '|', '97', '|', '98', '|', '99', '|', '100', '|', '101', '|', '102', '|', '103', '|', '104', '|', '105', '|', '106', '|', '107', '|', '108', '|', '109', '|', '110', '|', '111', '|', '112', '|', '113', '|', '114', '|', '115', '|', '116', '|', '117', '|', '118', '|', '119', '|', '120', '|', '121', '|', '122', '|', '65', '66', '|', '67', '|', '68', '|', '69', '|', '70', '|', '71', '|', '72', '|', '73', '|', '74', '|', '75', '|', '76', '|', '77', '|', '78', '|', '79', '|', '80', '|', '81', '|', '82', '|', '83', '|', '84', '|', '85', '|', '86', '|', '87', '|', '88', '|', '89', '|', '90', '|', '97', '|', '98', '|', '99', '|', '100', '|', '101', '|', '102', '|', '103', '|', '104', '|', '105', '|', '106', '|', '107', '|', '108', '|', '109', '|', '110', '|', '111', '|', '112', '|', '113', '|', '114', '|', '115', '|', '116', '|', '117', '|', '118', '|', '119', '|', '120', '|', '121', '|', '122', '|', '48', '49', '|', '50', '|', '51', '|', '52', '|', '53', '|', '54', '|', '55', '|', '56', '|', '57', '|', '|', '*', '.', '#1', '.', '|', '61', '#2', '.', '|', '42', '#3', '.', '|', '35', '.'],
    [('return WHITESPACE', 'WHITESPACE'), ('return ID', 'ID'), ('return EQUALS', 'EQUALS'), ('return TIMES', 'TIMES')]
)

test_file = sys.argv[1] if (len(sys.argv) > 1) else "./tests/slr-1-test.txt"
output_file = sys.argv[2] if (len(sys.argv) > 2) else "./out/output.txt"
output_type = sys.argv[3] if (len(sys.argv) > 3) else "analysis"

def return_token(found_token):

    WHITESPACE = "WHITESPACE"
    ID = "ID"
    EQUALS = "EQUALS"
    TIMES = "TIMES"

    if (found_token == WHITESPACE):
        return WHITESPACE
    if (found_token == ID):
        return ID
    if (found_token == EQUALS):
        return EQUALS
    if (found_token == TIMES):
        return TIMES

simulate_yalex_file(test_file, output_file, dfa, output_type, return_token)
