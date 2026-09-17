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
# r'[02468][A-Z]*[02468]'
from pydoc import stripid
# import re
# with open("24_23381.txt") as f:
#     data = f.read().strip()
# matches = re.findall(r'[02468][A-Z]*[02468]',data)
# print (len(max(matches,key=len)))
###################################################################
# №8837
# import re
# with open("24-371.txt") as f:
#     data = f.read()
# pattern = r'[^ .](?:[A-Z ]*[A-Z])?\.'
# matches =[match.group() for match in re.finditer(pattern,data)]
# ans = 0
# for match in matches:
#     if not any (char in match for char in 'XYZ'):
#         ans = max(ans, len(match))
# print(ans)
# for i in'XYZ': match = matc
import re
with open("../task -1 /24-371.txt") as f:
    data = f.read()
pattern = r'[^.]+\.'
matches = [match.group() for match in re.finditer(pattern,data)]
ans = 0
for match in matches:
    if match.count('M') >=112:
        while match.count('M') > 112:
            match = match[:-1]
        ans = max(ans, len(match))
print(ans)
# import re
# with open("24-371.txt") as f:
#     data = f.read()
# pattern = r'[^.]+\.'
# matches = [match.group() for match in re.finditer(pattern, data)]
# ans = 0
# for match in matches:
#     if match.count('M') == 112:
#         ans = max(ans, len(match))
# print(ans)
# import re
#
# with open(r"Task-24\files\24-371.txt") as f:
#     data = f.read()
# pattern = r'[A-Z]([A-Z ]*[A-Z])?\.'
# matches = [match.group() for match in re.finditer(pattern, data)]
#
# ans = 0
# for match in matches:
#     if not any(char in match for char in 'XYZ'):
#         ans = max(ans, len(match))
#     elif len(match) > ans:
#         # Вариант решения 1
#         r = len(match) - 1
#         while match[r] not in 'XYZ':
#             r -= 1
#         ans = max(ans, len(match[r + 1:].lstrip()))
#
#         # Вариант решения 2
#         for i in 'XYZ': match = match.replace(i, '*')
#         match = match.split('*')[-1].lstrip()
#         ans = max(ans, len(match))
#
# print(ans)
