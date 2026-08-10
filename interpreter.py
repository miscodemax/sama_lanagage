import sys
from pathlib import Path
import re

def combinaisons(line, idx):

    error_message = f'erreur de syntaxe a la ligne {idx} essaye "wax"'

    if not line.startswith('wax'):
        print(error_message)

    line = line[4:].strip()

    parts = re.split(r'\s+dolli\s+', line)
    parts_copy = parts.copy()
    

    for i, part in enumerate(parts):
        string_pattern = re.match(r'^"(.*)"$', part)
        number_pattern = re.match(r'^(-?\d+(?:\.\d+)?)$', part)

        if string_pattern:
            parts_copy[i] = parts_copy[i].strip('"')


        elif number_pattern:
            parts[i] = float(parts[i])

        else:
            print(error_message)


    return ('').join(parts_copy)
    

if len(sys.argv) == 1:
    print('aucun fichier trouvable')

else:
    filename = Path(sys.argv[1])

    if filename.suffix != '.wollof':
        print('erreur fichier wollof introuvable!')

    else:

        with open(filename, 'r', encoding='utf-8') as f:
            code = f.readlines()

        for idx, line in enumerate(code):

            line = line.strip()
            combi = 'dolli' in line
            

            string_pattern = r'^wax\s+"(.*)"$'
            number_pattern = r'^wax\s+(-?\d+(?:\.\d+)?)$'

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

            else:
                print(f'erreur de syntaxe ligne {idx}')