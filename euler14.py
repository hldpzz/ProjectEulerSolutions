def makechain(n):
  chain = [n]
  crr = n

  while crr!=1:
    if crr%2==0:
      crr=crr//2
      chain.append(crr)
    else:
      crr=(3*crr)+1
      chain.append(crr)

  return chain

start = 1000000


longestChain = []
longest_n = 0
while start!=0:
  current_chain = makechain(start)
  print(start)
  if len(current_chain)>len(longestChain):
    longestChain=current_chain
    print(longestChain)
    longest_n=start
  start-=1

print(longest_n)
