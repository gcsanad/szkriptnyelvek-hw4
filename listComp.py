
print("1.Feladat")
eredeti = ['auto', 'villamos', 'metro']
valtozott = [n.upper()+'!' for n in eredeti]


print(eredeti)
print(valtozott)

print("2.Feladat")
nevek = ['aladar', 'bela', 'cecil']
kezdobetu = [n[0].upper()+n[1:] for n in nevek]

print(nevek)
print(kezdobetu)

print("3.Feladat")
nullak = [0 for n in range(10)]
print(nullak)


print("4.Feladat")
szamok = list(range(1, 11))
dupla = [i*2 for i in szamok]
print(dupla)