def isprime(n):
  for i in range(2,n):
    if n%i==0:
      return False

  return True


primes = []
start =104729
while len(primes)<10002:
  print(len(primes))
  if isprime(start):
    primes.append(start)
    start+=1
  else:
    start+=1

print(primes)
