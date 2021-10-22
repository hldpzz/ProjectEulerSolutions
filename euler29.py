a = [n for n in range(2,101)]
b = [n for n in range(2,101)]
prods = []
prods_unique = []
for k in a:
  for i in b:
    prods.append(k**i)

for p in prods:
  if p not in prods_unique:
    prods_unique.append(p)
  else:
    continue


print(len(prods_unique))
