"""
Universidad del Valle de Guatemala
(CC3071) Diseño de Lenguajes de Programación
Santiago Taracena Puga (20017)
"""

# Función para simular un archivo .yal.
def simulate_yalex_file(path, dfa, return_token):

    # Archivo en forma de string inicial.
    file_string = ""

    # Lectura del archivo de prueba.
    with open(path, "r", newline="") as file:
        for line in file:
            for char in line:
                file_string += char

    # Conversión del string a una lista de ASCII.
    file_string = [str(ord(char)) for char in file_string if (ord(char) != 13)]

    # Variables de la simulación y lookahead máximo
    i, j = 0, 0
    MAX_LOOK_AHEAD = 3

    # Mientras aún quede archivo para simular.
    while (len(file_string) > 0):

        # String a simular (inicia con el primer caracter del archivo).
        if (j < len(file_string)):
            simulated_string = [file_string[j]]
        else:
            break

        # Resultado de la simulación del string y obtención del token.
        result, found_token = dfa.simulate(simulated_string)
        token = return_token(found_token)

        # Lookahead inicial.
        look_ahead = 1

        # Si no se aceptó el string, se lanza un error léxico.
        if (not result):

            # Se imprime el error léxico y se reinicia la simulación.
            print(f"Found lexical error: \"{''.join([chr(int(char)) for char in simulated_string])}\" with ASCII {simulated_string}\n")
            i += 1
            j = i

        # Si se aceptó el string, se prueba con el siguiente caracter hasta dar error léxico.
        while (result):

            # Almacenamiento del último token aceptado.
            last_token = token

            # Actualización del resultado de la simulación y obtención del token.
            result, found_token = dfa.simulate(simulated_string)
            token = return_token(found_token)

            # Si se aceptó el string, se agrega el siguiente caracter.
            if (result):

                # Nuevo índice si queda archivo por simular.
                i += 1 if (len(file_string) > 1) else 0

                # Agregado del siguiente caracter al string a simular.
                simulated_string.append(file_string[i])

                # Si sólo queda un último caracter en el archivo, se acaba la simulación.
                if (len(file_string) == 1):

                    # Impresión del último token y finalización de la simulación.
                    print(f"Found token {last_token}: \"{''.join([chr(int(char)) for char in simulated_string[:-1]])}\" with ASCII {simulated_string[:-1]}")
                    file_string = []
                    break

            # Si no se aceptó el string, se intenta utilizar el lookahead.
            else:

                # Se reinicia el string a simular.
                string_before_look_ahead = simulated_string.copy()

                # Ciclo que se ejecuta mientras el lookahead sea menor o igual al máximo y no se haya llegado al final del archivo.
                while ((look_ahead <= MAX_LOOK_AHEAD) and ((i + look_ahead) < len(file_string))):

                    # Se intenta simular el string con el lookahead.
                    look_ahead_simulated_string = simulated_string + [file_string[i + look_ahead]]
                    look_ahead_result, found_look_ahead_token = dfa.simulate(look_ahead_simulated_string)
                    look_ahead_token = return_token(found_look_ahead_token)
                    simulated_string = look_ahead_simulated_string.copy()

                    # Si se aceptó el string con el lookahead, se actualizan las variables.
                    if (look_ahead_result):
                        result = look_ahead_result
                        token = look_ahead_token
                        i += look_ahead
                        look_ahead = 1
                        break
                    else:
                        look_ahead += 1
                
                else:
                    print(f"Found token {last_token}: \"{''.join([chr(int(char)) for char in string_before_look_ahead[:-1]])}\" with ASCII {string_before_look_ahead[:-1]}\n")
                    file_string = file_string[i:]
                    i, j = 0, 0
                    simulated_string = [file_string[j]]
                    break

    print("\n")
