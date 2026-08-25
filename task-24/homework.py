# import re
# with open('../task-24/2942.txt') as f:
#     data = f.read().strip()
# matches = re.findall(r'(?:AB|AC)+', data)
# print(matches[:10])
# print(max(map(lambda x: len(x) // 2, matches)))
#
# import re
# with open('../task-24/244602.txt') as f:
#     data = f.read().strip()
# matches = re.findall(r'(?:[BCD][AO])+', data)

# print(max(len(x) // 2 for x in matches))
# #klmnklmnklmn
# pattern = r''
# import re
# with open("24_7600.txt") as f:
#     data = f.read().strip()
# matches = re.findall(r'[A-PT-Z]*(?:[QRS][A-PT-Z]+)*[QRS]?',data)
# print (len(max(matches,key=len)))
r'[02468][A-Z]*[02468]'
# import re
# with open("24_23381.txt") as f:
#     data = f.read().strip()
# matches = re.findall(r'[02468][A-Z]*[02468]',data)
# print (len(max(matches,key=len)))
###################################################################
# №8837
from re import *
with open() as f:
    data = f.readlines()