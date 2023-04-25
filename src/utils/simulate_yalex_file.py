"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

def simulate_yalex_file(path, dfa, return_token):
    file_string = ""

    with open(path, "r", newline="") as file:
        for line in file:
            for char in line:
                file_string += char

    file_string = [str(ord(char)) for char in file_string if (ord(char) != 13)]

    # print(file_string, "\n\n")

    i, j = 0, 0
    MAX_LOOK_AHEAD = 5

    # Mientras aún quede archivo para simular.
    while (len(file_string) > 0):

        # String anterior y string simulada.
        simulated_string = [file_string[j]]
        look_ahead = 1
        result, found_token = dfa.simulate(simulated_string)
        token = return_token(found_token)

        if (not result):
            print(f"Found lexical error: {''.join([chr(int(char)) for char in simulated_string])} with ASCII {simulated_string}\n")
            i += 1
            j = i

        while (result):
            last_token = token
            result, found_token = dfa.simulate(simulated_string)
            token = return_token(found_token)

            if (result):
                i += 1 if (len(file_string) > 1) else 0
                simulated_string.append(file_string[i])
                if (len(file_string) == 1):
                    print(f"Found token {last_token}: {''.join([chr(int(char)) for char in simulated_string[:-1]])} with ASCII {simulated_string[:-1]}")
                    file_string = []
                    break
            else:
                if ((i + look_ahead) < len(file_string)):
                    look_aheaded_simulated_string = simulated_string + [file_string[i + look_ahead]]
                    look_ahead_result, look_ahead_token = dfa.simulate(look_aheaded_simulated_string)

                    # print("simulating look_aheaded_simulated_string", ''.join([chr(int(char)) for char in look_aheaded_simulated_string]), "resulted in", look_ahead_result, "with token", look_ahead_token)
                    if (look_ahead_result):
                        simulated_string = look_aheaded_simulated_string.copy()
                        result = look_ahead_result
                        found_token = look_ahead_token
                        token = return_token(found_token)
                        i += look_ahead
                        look_ahead = 1
                        continue
                    # else:
                    #     if (look_ahead < MAX_LOOK_AHEAD):
                    #         simulated_string = look_aheaded_simulated_string.copy()
                    #         look_ahead += 1
                    #         i += 1
                    #         continue
                    #     else:
                    #         print(f"Found token {last_token}: {''.join([chr(int(char)) for char in simulated_string[:-1]])} with ASCII {simulated_string[:-1]}\n")
                    #         file_string = file_string[i:]
                    #         i, j = 0, 0
                    #         simulated_string = [file_string[j]]
                    #         break
                print(f"Found token {last_token}: {''.join([chr(int(char)) for char in simulated_string[:-1]])} with ASCII {simulated_string[:-1]}\n")
                file_string = file_string[i:]
                i, j = 0, 0
                simulated_string = [file_string[j]]
                break

    print("\n")
