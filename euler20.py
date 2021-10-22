def fact(n):
  if n==1:
    return n
  else:
    return n*fact(n-1)

f100 = str(fact(100))

tot=0

for n in f100:
  tot+=int(n)

print(tot)
