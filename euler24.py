import itertools

s = '0123456789'

perms = itertools.permutations(s,10)
count = 0
obj = []
for i in perms:
  print(count)
  count+=1
  if count==1000000:
    obj.append(i)
    break


print(obj)
