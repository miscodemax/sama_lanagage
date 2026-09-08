import sys
from pathlib import Path
import re


variables: dict[str, int] = {}

def operations(a: int | float, operation: str, b: int | float) -> int | float | bool:

    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b


    
    

def combinaisons(line: list[str | int], idx: int) -> str:

    error_message = f'erreur de syntaxe a la ligne {idx} essaye "wax"'

    if not line.startswith('wax'):
        print(error_message)

    line = line[4:].strip()

    parts = re.split(r'\s+dolli\s+', line)
    parts_copy = parts.copy()
    

    for i, part in enumerate(parts):

        if part in variables:
            parts[i] = str(variables[parts[i]])
            parts_copy[i] = str(variables[parts_copy[i]])
            
                   

        string_pattern = re.match(r'^"(.*)"$', parts[i])
        number_pattern = re.match(r'^(-?\d+(?:\.\d+)?)$', parts[i])
        pattern = r'^(-?\d+(?:\.\d+)?)\s*([+\-*/%])\s*(-?\d+(?:\.\d+)?)$'
        var_op_pattern = r'^([a-zA-Z_]\w*)\s*([+\-*/%])\s*([a-zA-Z_]\w*)$'
        var_op_match = re.match(var_op_pattern, parts[i])
        operation_pattern = re.match(pattern, parts[i])


       
    

        if string_pattern:
            parts_copy[i] = parts_copy[i].strip('"')


        elif number_pattern:
            parts[i] = float(parts[i])

        elif operation_pattern:
            a = float(operation_pattern.group(1))
            operation = operation_pattern.group(2)
            b = float(operation_pattern.group(3))
            resultats = operations(a, operation, b)

            if resultats == False:
                print(f'Erreur a la ligne {idx} erreurr de frappe operation')

            parts_copy[i] = str(resultats)

        elif var_op_match:
            first_var = variables[var_op_match.group(1)]
            op = var_op_match.group(2)
            second_var = variables[var_op_match.group(3)]
            res = operations(first_var, op, second_var)

            if res == False:
                print(f'Erreur a la ligne {idx} erruer de frappe operation')
            
            parts_copy[i] = str(res)
        else:
            print(error_message)


    return ('').join(parts_copy)
    




if len(sys.argv) == 1:
    print('aucun fichier trouvable')

else:
    filename: str = Path(sys.argv[1])

    if filename.suffix != '.wollof':
        print('erreur fichier wollof introuvable!')

    else:

        with open(filename, 'r', encoding='utf-8') as f:
            code = f.readlines()

        for idx, line in enumerate(code):

            line = line.strip()
            combi = 'dolli' in line

            if len(line) == 0:
                continue
            

            string_pattern = r'^wax\s+"(.*)"$'
            number_pattern = r'^wax\s+(-?\d+(?:\.\d+)?)$'
            pattern = r'^wax\s+(-?\d+(?:\.\d+)?)\s*([+\-*/%])\s*(-?\d+(?:\.\d+)?)$'
            operation_pattern = re.match(pattern, line)
            variable_pattern = r'^([a-zA-Z_]\w*)\s+moy\s+(.+)$'
            match_variable = re.match(variable_pattern, line)


            string_match = re.match(string_pattern, line)
            number_match = re.match(number_pattern, line)

            if string_match and not combi:

                message = string_match.group(1)
                print(message)

            elif number_match and not combi:

                message = number_match.group(1)
                print(message)

            elif combi:
                print(combinaisons(line, idx))

            elif operation_pattern:
                a = float(operation_pattern.group(1))
                operation = operation_pattern.group(2)
                b = float(operation_pattern.group(3))
                resultats = operations(a, operation, b)
    
                if resultats == False:
                    print(f'Erreur a la ligne {idx} erreur de frappe operation')

                print(resultats)

            elif match_variable:
                var_name = match_variable.group(1)
                var_value = match_variable.group(2)

                string_var_pattern = re.match(r'^"(.*)"$', var_value)
                number_var_pattern = re.match(r'^(-?\d+(?:\.\d+)?)$', var_value)

                if number_var_pattern:
                    var_value = float(var_value)

                variables[var_name] = var_value

            else:
                print(f'erreur de syntaxe ligne {idx}')


