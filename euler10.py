

def isprime(n):

  if n==1:
    return True
  if n==2:
    return True

  for k in range(2,n):
    if n%k==0:
      return False
  return True


toCheck = [n for n in range(1,2000000)]
toSkip = {}
total = 0


for i in toCheck:
  if i in toSkip:
    print('skipped',i)
    continue
  else:
    if isprime(i):
      if i!=1:
        print('found prime',i)
        total+=i
        for k in range(2000000):
          toSkip[i*k]=True


print(total)
