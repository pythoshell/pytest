
def total(initial = 5, *num, **key):
   count = initial
   print('Here Count',count)
   for n in num:
      print("here n",n)
      count+=n
   for k in key:
      print('Here K',k)
      count+=key[k]
   return count
print(total(100,2,3, clouds=50, stars=100))