import itertools
import numpy as np
possible = [a for a in range(1,1000)]

combs = itertools.combinations(possible,2)


def solve():
  for comb in combs:
    a,b = comb
    print(a,b)

    if a+b+np.sqrt(pow(a,2)+pow(b,2))==1000:
        return(a,b)


print(solve())
