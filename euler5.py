start = 2520




def isdiv(n):
  nums = [k for k in range(1,20)]

  for k in nums:
    if n%k!=0:
      return False

  return True

while not isdiv(start):
  print(start)
  start+=2520

print(start)
