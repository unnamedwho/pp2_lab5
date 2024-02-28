import re


with open('row.txt', 'r') as file:
    smth = file.read()
#ex - 1

x = re.compile(r'ab*')
m = x.findall(smth)
print("<<ex - 1>>")
print(m)

#ex - 2

x = re.compile(r'ab{2, 3}')
m = x.findall(smth)
print("<<ex - 2>>")
print(m)


#ex - 3

x = re.compile(r'[a-z]+_[a-z]+')
m = x.findall(smth)
print("<<ex - 3>>")
print(m)

#ex - 4

x = re.compile(r'[A-Z][a-z]+')
m = x.findall(smth)
print("<<ex - 4>>")
print(m)

#ex - 5

x = re.compile(r'a.*b$')
m = x.findall(smth)
print("<<ex - 5>>")
print(m)

#ex - 6

x = re.sub("\s", "," or ":" , smth)
print("<<ex - 6>>")
print(x)

#ex - 7

x = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), smth)
print("<<ex - 7>>")
print(x)

#ex - 8

x = re.split(r'([A-Z])', smth)
print("<<ex - 8>>")
print(x)

#ex - 9

x = re.sub(r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))', r'\1 ', smth)
print("<<ex - 9>>")
print(x)

#ex - 10

x = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', smth)
print("<<ex - 10>>")
print(x)







