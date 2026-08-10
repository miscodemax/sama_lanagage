import sys
from pathlib import Path
import re

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

            string_pattern = r'^wax\s+"(.*)"$'
            number_pattern = r'^wax\s+(-?\d+(?:\.\d+)?)$'

            string_match = re.match(string_pattern, line)
            number_match = re.match(number_pattern, line)

            if string_match:

                message = string_match.group(1)
                print(message)

            elif number_match:

                message = number_match.group(1)
                print(message)

            else:
                print(f'erreur de syntaxe ligne {idx}')