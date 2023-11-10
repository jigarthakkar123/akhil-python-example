d={123:"Akhil",908:"Prashant",567:"Jigar",434:"Shubham"}

print(d)
print(d[123])
print(d.get(908))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(567))
print(d)
print(d.popitem())
print(d)
d1={1:"Jigar",2:"Ajay"}
d.update(d1)
print(d)

for i in d:
    print(i," : ",d[i])
