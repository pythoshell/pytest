from Library import lib_windows_general

def total(initial = 5, *num, **key):
   count = initial
   for n in num:
      count+=n
   for k in key:
      count+=key[k]
   return count
print(total(100,2,3, clouds=50, stars=100))



