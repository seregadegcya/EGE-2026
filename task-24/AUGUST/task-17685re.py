num = r"([1-9][0-9]*|0)"
zero = r'({num}\*)*0(\*{num})*'
pattern = rf"({zero}\+)*{zero}"