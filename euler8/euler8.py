def prodarr(arr):
  prod = 1

  for n in arr:
    prod*=n

  return prod

number = open('./number.txt')
nstr = number.read()


prods = []
holds13 = []
for n in nstr:
  if len(holds13)==13:
    prods.append(prodarr(holds13))
    holds13=[]
  holds13.append(int(n))




print(max(prods))
