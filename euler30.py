
def powerSum5(n):
  nstr = str(n)
  length = len(nstr)
  digits = [int(k) for k in nstr]
  digitspower = [k**5 for k in digits]

  if sum(digitspower)==n:
    return True

  else:
    return False

powerdigits = []


for i in range(2,355000):
  
  if powerSum5(i):
    powerdigits.append(i)
    print(powerdigits)

arr = [4150, 4151, 54748, 92727, 93084, 194979]
print(sum(arr))
