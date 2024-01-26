
print("count".center(60, "-"))
l1 =  [1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2,2, 1, 2, 3, 1, 1, 1,1,1, 1, 2, 3, 1, 2,1, 1,1, 1,2,2,2,2,2,2,2, 1,1, 1,1 , 1 ,1,1 ,1, 1, 1]

print(f"1 : {l1.count(1)}")
print(f"2 : {l1.count(2)}")
print(f"3 : {l1.count(3)}")
print(f"5 : {l1.count(5)}")

print("index".center(60, "-"))

l1 =  [1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2,2, 1, 2, 3, 1, 1, 1,1,1, 1, 2, 3, 1, 2,1, 1,1, 1,2,2,2,2,2,2,2, 1,1, 1,1 , 1 ,1,1 ,1, 1, 1]

print(l1.index(3))
print(l1.index(3, l1.index(3) + 1))
print(l1.index(3, l1.index(3, l1.index(3) + 1) + 1))

print("clear".center(60, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")
l1.clear()
print(f"l1 :{l1}")

print("copy".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

# copy elements of l1 into l2
l2 = l1              # shallow copy - copies the data with the address

print(f"l2 before :{l2}")

l2.append(6)
l2.append(7)
l2.append(8)
l2.append(9)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print()
print("-" * 60)
print()

l3 = [6, 7, 8, 9, 10]
print(f"l3 before :{l3}")

# copy from l3 to l4
l4 = l3.copy()              # deep copy - copies only values

print(f"l4 before :{l4}")

l4.extend([11, 12, 13, 14, 15])
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print()
print("-" * 60)
print()

l5 = [10, 20, 30, 40, [1, 2, 3, 4, 5], 50]
print(f"l5 before :{l5}")

# copy values for l5 to l6
l6 = l5.copy()

print(f"l6 before :{l6}")

l6[4].extend(list(range(6, 11)))
print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print()
print("-" * 60)
print()

from copy import deepcopy
l7 = [2, 4, 6, [1, 3, 5, 7, 9], 8, 10]
print(f"l7 before :{l7}")

l8 = deepcopy(l7)          # deepcopy will only share the data
print(f"l8 before :{l8}")

l8[3].extend([11,13,15,17])
print(f"l8 after :{l8}")
print(f"l7 after :{l7}")

