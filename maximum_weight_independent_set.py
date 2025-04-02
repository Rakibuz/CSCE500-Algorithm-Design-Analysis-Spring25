def MWIS(n, tree):
    from collections import defaultdict

    # Initialize adjacency list
    adj_list = defaultdict(list)
    weights = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if i - 1 < len(tree):  # Ensure we don't go out of range
            p, w = tree[i - 1]
            if i != 1:
                adj_list[p].append(i)
            weights[i] = w
    # DP arrays to store results for each node
    dp = [[0, 0] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    def dfs(node):
        visited[node] = True
        dp[node][0] = 0 # Maximum weight excluding the current node
        dp[node][1] = weights[node] # Maximum weight including the current node
        
        for child in adj_list[node]:
            if not visited[child]:
                dfs(child)
                 # Update DP values based on the child nodes
                dp[node][0] += max(dp[child][0], dp[child][1])
                dp[node][1] += dp[child][0]
     # Start DFS from the root node (node 1)
    dfs(1)
    # The result is the maximum of including or excluding the root node
    return max(dp[1][0], dp[1][1])

# Example input
n = 11
tree = [(0, 15), (1, 8), (1, 16), (1, 18), (2, 3), (2, 5), (2, 5), (3, 7), (4, 2), (4, 9),(6,4)]

# Output the result
print(MWIS(n, tree))
