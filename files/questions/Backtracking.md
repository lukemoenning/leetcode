- [ ] Done with help 
- [x] Done on own

- [ ] [[Backtracking#[Subsets (78)](https://leetcode.com/problems/subsets/description/) |Subsets - 08/28/2023]]
- [ ] [[Backtracking#[Permutations (46)](https://leetcode.com/problems/permutations/description/) |Permutations - 09/04/2023]]
- [ ] [[Backtracking#[Maximum Length of a Concatenated String with Unique Characters (1239)](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/) |Maximum Length of a Concatenated String with Unique Characters - 01/22/2024]]


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
## [Maximum Length of a Concatenated String with Unique Characters (1239)](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/)
###### *01/22/2024*

###### Psuedo Code
``` 
# backtracking
```

###### Python Solution
```python
def maxLength(self, arr: List[str]) -> int:
	if not arr:
		return 0

	N = len(arr)

	def is_unique(s):
		return len(s) == len(set(s))

	def recur(i, s):
		# base case
		if i == N:
			return len(s)

		# recursive step
		leave = recur(i+1, s)
		take = recur(i+1, s+arr[i]) if is_unique(s+arr[i]) else -1

		return max(leave, take)

	return recur(0, '')
```

###### Runtime Complexity
```
O(2^n)
```

###### Space Complexity
```
O(2^n)
```


---