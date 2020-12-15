string = 'half,hall,hallo,hate,heart,heavy'
a = string[:string.find('h') + 1]
b = string[string.find('h') + 1:string.rfind('h')]
c = string[string.rfind('h'):]
s = a + b.replace('h', 'H') + c
print(s)

