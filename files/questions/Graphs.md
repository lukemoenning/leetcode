- [ ] Done with help 
- [x] Done on own

- [ ] [[Graphs#[Number of Islands (200)](https://leetcode.com/problems/number-of-islands/description/) |Number of Islands - 11/01/2023]]
- [ ] [[Graphs#[Max Area of Island (695)](https://leetcode.com/problems/max-area-of-island/description/) |Max Area of Island - 11/01/2023]]



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
O(n*m)
```

###### Space Complexity
```
O(n*m)
```


--- 
## [Max Area of Island (695)](https://leetcode.com/problems/max-area-of-island/description/)
###### *11/01/2023*

###### Psuedo Code
``` 
# iterate each cell, checking for new islands, 
# if we find a new island, discover the entire thing with dfs/bfs, updating max_found accordingly
```

###### Python Solution
```python
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
	if not grid:
		return 0

	N = len(grid)
	M = len(grid[0])
	vis = set()
	largest_island = 0

	def getValidMoves(x, y):
		valid_moves = []
		potential_moves = [(0,1), (0,-1), (1,0), (-1,0)]

		for dx, dy in potential_moves:
			if 0 <= (x + dx) < N and 0 <= (y + dy) < M:
				valid_moves.append((x+dx, y+dy))

		return valid_moves

	# assuming input here is valid and unvisited
	def dfs(x, y):
		curr_size = 0
		stack = [(x, y)]

		while stack:
			curr_x, curr_y = stack.pop()
			if (curr_x, curr_y) in vis:
				continue

			vis.add((curr_x, curr_y))
			curr_size += 1
			moves = getValidMoves(curr_x, curr_y)
			for move in moves:
				new_x, new_y = move
				if grid[new_x][new_y] == 1:
					stack.append((new_x, new_y))

		return curr_size
	
	for x in range(N):
		for y in range(M):
			# check for a new island
			if grid[x][y] == 1 and (x, y) not in vis:
				# find size of island
				size = dfs(x, y)
				largest_island = max(largest_island, size)
	
	
	return largest_island
```

###### Runtime Complexity
```
O(n*m)
```

###### Space Complexity
```
O(n*m)
```


---