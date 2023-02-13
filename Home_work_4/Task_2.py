n = int(input())
Berry_tree = [int(i) for i in range(n)]
Berry_tree_top = 0
for i in range(n):
    Berry_sum = Berry_tree[i-1]+ Berry_tree[i]+ Berry_tree[i+1 if i<n-1 else 0]
    if Berry_sum>Berry_tree_top:
        Berry_tree_top = Berry_sum
print(Berry_tree_top)