
def find_farthest_orbit(nums):
    return max([(a[0]*a[1]*3.14,a) for a in nums if a[0]!=a[1]])[1]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
orbits = [(1, 100), (3, 4)]
# print(*find_farthest_orbit(orbits))
print(*find_farthest_orbit(orbits))