nfile = open('./number.txt')
obj = []
objfilter = []
for line in nfile:
  obj.append(line[:len(line)])

for s in obj:
  cstr = '\n'

  if cstr in s:
    newstr = s.replace(cstr,'')
    objfilter.append(newstr)
  else:
    objfilter.append(s)

total = 0

for n in objfilter:
  total+=int(n)

print(total)
