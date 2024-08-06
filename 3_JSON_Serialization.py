# Serialization = 'The process of translating a data structure or object state into a format that can
# be stored ( for example, in a file or memory data buffer) or transmitted (for example over a computer
# network ) and reconstructed later (possibly in a different computer environment)'

import json

languages = [
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]

file_name = 'text.json'

with open(file_name, 'w', encoding='utf-8') as testfile:
    json.dump(languages, testfile)   # dump method is used to serialized data
