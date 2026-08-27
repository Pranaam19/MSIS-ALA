from vec import Vec

v1 = Vec((0, 1, 1.03))
v2 = Vec((1, 2, 3))
print(v1)
v3 = 2.2 * v1
v3 *= 5
    # v3 = 1 + v3
    # print(v3)
    # v2 = v1 + v3
    # print(v1 + v3)
    # v1 *= 5
print(v1)
v4 =-v1
print(v4)
o1 = Vec.zeros(3)
print(o1)
print(v1+v2)
#print(-(v1 + v3))


