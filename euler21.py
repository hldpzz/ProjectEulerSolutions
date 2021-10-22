import itertools

srange = [k for k in range(1,10000)]

def sumdiv(n):
  tot = 0

  for i in range(1,n):
    if n%i==0:
      tot+=i

  return tot

total = 0

for n in srange:
  pair = sumdiv(n)
  if n!=pair:
    
    if sumdiv(pair)==n:
      print(n,pair)
      total+=n
      continue
  
print(total)

