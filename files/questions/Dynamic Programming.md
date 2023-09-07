- [ ] Done with help 
- [x] Done on own

- [ ] [[Dynamic Programming#[Climbing Stairs (70)](https://leetcode.com/problems/climbing-stairs/description/) |Climbing Stairs - 09/06/2023]]

- [ ] [[Dynamic Programming#[Mine Cost Climbing Stairs (746)](https://leetcode.com/problems/min-cost-climbing-stairs/description/) |Mine Cost Climbing Stairs - 09/06/2023]]


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
## [Mine Cost Climbing Stairs (746)](https://leetcode.com/problems/min-cost-climbing-stairs/description/)
###### *09/06/2023*

###### Psuedo Code
``` 
# build up to the solution
# the price for i is min(dp[i-1]+cost[i], dp[i-2]+cost[2])
# need to build to one beyond the list since we want to reach the top
```

###### Python Solution
```python
def minCostClimbingStairs(self, cost: List[int]) -> int:
	N = len(cost)
	dp = [0] * (N+1)

	for i in range(2,N+1):
		dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

	return dp[N]
```

###### Runtime Complexity
```
O(n)
```

###### Space Complexity
```
O(n)
```


---