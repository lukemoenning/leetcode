- [ ] Done with help 
- [x] Done on own

- [ ] [[Graphs#[Number of Islands (200)](https://leetcode.com/problems/number-of-islands/description/) |Number of Islands - 11/01/2023]]



---
## [Number of Islands (200)](https://leetcode.com/problems/number-of-islands/description/)
###### *11/01/2023*

###### Psuedo Code
``` 
# find unvisited islands, dfs to uncover entire island, only increment count when finding a new island
```

###### Python Solution
```python
def numIslands(self, grid: List[List[str]]) -> int:
	if not grid: 
		return 0

	N = len(grid)
	M = len(grid[0])
	vis = set()
	num = 0

	def getValidMoves(i, j):
		moves = []
		if i + 1 < N:
			moves.append((i+1, j))
		if i - 1 >= 0:
			moves.append((i-1, j))
		if j + 1 < M:
			moves.append((i, j+1))
		if j - 1 >= 0:
			moves.append((i, j-1))

		return moves


	# def dfs(i, j):
	#     vis.add((i,j))
	#     valid_moves = getValidMoves(i,j)

	#     for move in valid_moves:
	#         di, dj = move
	#         if grid[di][dj] == '1' and (di,dj) not in vis:
	#             dfs(di, dj)

	def dfs(i, j):
		stack.append((i,j))

		while stack:
			vis.add(stack[-1])
			i, j = stack.pop()
			moves = getValidMoves(i,j)
			for move in moves:
				di, dj = move
				if grid[di][dj] == '1' and (di,dj) not in vis:
					stack.append((di,dj))

	stack = []
	for row in range(N):
		for col in range(M):
			if grid[row][col] == '1' and (row, col) not in vis:
				num += 1
				dfs(row, col)
				
	return num
```

###### Runtime Complexity
```
O(n * m)
```

###### Space Complexity
```
O(n * m)
```


---