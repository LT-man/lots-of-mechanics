import numpy as np
list = [12, 12, 213, 765, 34, 86]
one = np.array(list)
print(one[2:5])
list2 = [[234567, 456789, 56789, 999999], [213, 1234, 6454, 98], [123, 23, 12, 433]]
two = np.array(list2)
print(two[1:5, 1:3])
ds = np.arange(1, 50)
print(ds[1:49:2])
print(ds[::-1])
res = ds.reshape(7, 7)
print(res[4:7, 4:7])
even = ds[ds > 5]
print(even)
perc = ds[ds % 5 == 0]
print(perc)
list3 = np.arange(1, 26).reshape(5, 5)
list4 = np.arange(26, 51).reshape(5, 5)
print(list3)
print(list4)
print(list3 + list4)
print(list3 + list4 * list3 / list4 / list3 +list4 - list3)
def solve (x):
    return x + (2 * x ** 2) + 3
print(solve(list4))