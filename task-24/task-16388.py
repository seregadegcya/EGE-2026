import re
with open('../task-24/24_16388.txt') as f:
    data = f.read().strip()
matches = re.findall(r'(LMN|MN|N)?(KLMN)+(KLM|KL|k)?', data)
print (len(max(matches, key=len)))