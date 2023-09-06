- [ ] Done with help 
- [x] Done on own

- [ ] [[Dynamic Programming#[Climbing Stairs (70)](https://leetcode.com/problems/climbing-stairs/description/) |Climbing Stairs - 09/06/2023]]



---
## [Climbing Stairs (70)](https://leetcode.com/problems/climbing-stairs/description/)
###### *09/06/2023*

###### Psuedo Code
``` 
# dp or fibonacci
# 1 for 1 step, 2 for 2, etc
```

###### Python Solution
```python
def climbStairs(self, n: int) -> int:
	nMinus2 = 0
	nMinus1 = 1

	for num in range(n):
		curr = nMinus2 + nMinus1
		nMinus2 = nMinus1
		nMinus1 = curr

	return curr

	###################

def climbStairs(self, n: int) -> int:
	if n == 1:
		return 1
	
	dp = [1] * (n)
	dp[1] = 2

	for num in range(2,n):
		dp[num] = dp[num-2] + dp[num-1]

	return dp[n-1]
```

###### Runtime Complexity
```
O(n)
```

###### Space Complexity
```
O(1)
```


---