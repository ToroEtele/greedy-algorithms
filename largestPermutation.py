# Given an array of a random permutation of numbers from 1 to N. Given B, the number of swaps in A that we can make
# Find the largest permutation

A = [3, 2, 4, 1, 5]
B = 3

i = 0
_max = len(A)
d = {x: i for i, x in enumerate(A)}
# {3: 0, 2: 1, 4: 2, 1: 3, 5: 4}
# for index, element in iterable

print(_max)

while B and i < len(A):
  j = d[_max] #legnagyobb elem poziciója a sorból 
  if i == j:  #ha a helyén van nem módosítjuk
    pass
  else:
    B -= 1    #a cserék számát csökkentjük, és végrehajtjuk a cserét
    A[i], A[j] = A[j], A[i]
    d[A[i]], d[A[j]] = d[A[j]], d[A[i]]

  i += 1      #kezdőpont értéke nő, mivel az elem a helyére került
  _max -= 1   #a legnagyobb elem az egyel kisebb lesz mivel a nagyobbak helyükre kerültek

#print(d)