strg="India got its independence in 1947 .India became republic in 1956. Article 370 is abolished in 2019 ."
strg = str.replace('.','')
icount = strg.count("India")
print('Count of india ',icount)
print(strg)
aftersplit = strg.split(" ")
print(aftersplit)
wcount = 0
icount = 0
sumofdigit = 0
for n in aftersplit:
    if (len(n) > 0):
        wcount = wcount+1
        if (n.isdigit()):
            sumofdigit = sumofdigit + int(n) 
print('Word count',wcount)
print('Sum of digit ',sumofdigit)