- [ ] Done with help 
- [x] Done on own

- [ ] [[Backtracking#[Subsets (78)](https://leetcode.com/problems/subsets/description/) |Subsets - 08/28/2023]]
- [ ] [[Backtracking#[Permutations (46)](https://leetcode.com/problems/permutations/description/) |Permutations - 09/04/2023]]


---
## [Subsets (78)](https://leetcode.com/problems/subsets/description/)
###### *08/28/2023*

###### Psuedo Code
``` 
# conceptually, build a state space tree with we want the last level
# dfs through state space tree, either take, use a single list to keep track of current subset, backtracking to modify it
```

###### Python Solution
```python
def subsets(self, nums: List[int]) -> List[List[int]]:
	res = []
	sub = []

	def dfs(i=0):
		if i == len(nums):
			res.append(sub.copy())
			return 

		# take current
		sub.append(nums[i])
		dfs(i+1)

		# leave current
		sub.pop()
		dfs(i+1)
	
	dfs()
	return res
```

###### Runtime Complexity
```
O(n * 2^n)
```

###### Space Complexity
```
O(n)
```


---
## [Permutations (46)](https://leetcode.com/problems/permutations/description/)
###### *09/04/2023*

###### Psuedo Code
``` 
# backtracking, for each unused number: append, backtrack, pop
```

###### Python Solution
```python
def permute(self, nums: List[int]) -> List[List[int]]:
	N = len(nums)
	res = []

	def backtrack(i, curr):
		if i > N:
			return 

		if len(curr) == N:
			res.append(curr.copy())
			return

		for num in nums:
			if num not in curr:
				curr.append(num)
				backtrack(i+1, curr)
				curr.pop()

	backtrack(0, [])
	
	return res
```

###### Runtime Complexity
```
O(n * n!)
```

###### Space Complexity
```
O(n)
```


---