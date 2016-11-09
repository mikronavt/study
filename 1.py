code1 = input()
code2 = input()
str1 = input()
str2 = input()
crypt = {}
encrypt = {}
for i in range(0, len(code1)):
    crypt.update({code1[i]: code2[i]})
    encrypt.update({code2[i]: code1[i]})
#print(crypt)
#print(encrypt)
out1 = ""
out2 = ""
for i in str1:
    out1 = out1 + crypt.get(i)
for i in str2:
    out2 = out2 + encrypt.get(i)
print(out1)
print(out2)