- [ ] Done with help 
- [x] Done on own

- [ ] [[Dynamic Programming#[Climbing Stairs (70)](https://leetcode.com/problems/climbing-stairs/description/) |Climbing Stairs - 09/06/2023]]
- [ ] [[Dynamic Programming#[Mine Cost Climbing Stairs (746)](https://leetcode.com/problems/min-cost-climbing-stairs/description/) |Mine Cost Climbing Stairs - 09/06/2023]]
- [ ] [[Dynamic Programming#[House Robber (198)](https://leetcode.com/problems/house-robber/description/) |House Robber - 09/07/2023]]
- [ ] [[Dynamic Programming#[House Robber II (213)](https://leetcode.com/problems/house-robber-ii/) |House Robber II - 09/09/2023]]
- [ ] [[Dynamic Programming#[Longest Palindromic Substring (5)](https://leetcode.com/problems/longest-palindromic-substring/description/) |Longest Palindromic Substring - 09/11/2023]]
- [ ] [[Dynamic Programming#[Palindromic Substrings (647)](https://leetcode.com/problems/palindromic-substrings/description/) |Palindromic Substrings - 09/12/2023]]
- [ ] [[Dynamic Programming#[Decode Ways (91)](https://leetcode.com/problems/decode-ways/description) |Decode Ways - 12/25/2023]]
- [ ] [[Dynamic Programming#[Number of Dice Rolls With Target Sum (1155)](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/) |Number of Dice Rolls With Target Sum - 12/26/2023]]
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
## [House Robber (198)](https://leetcode.com/problems/house-robber/description/)
###### *09/07/2023*

###### Psuedo Code
``` 
# could use memo and recursion to build a tree, for each index we want the max(current + 2back, 1back)
# instead, we can build up to in similiar to fibonacci 
```

###### Python Solution
```python
# def rob(self, nums: List[int]) -> int:
#     N = len(nums)

#     def recur(i):
#         if i < 0:
#             return 0

#         return max(recur(i-2)+nums[i], recur(i-1))

#     return recur(N-1)

##########################

# def rob(self, nums: List[int]) -> int:
#     N = len(nums)
#     memo = {}

#     def recur(i):
#         if i < 0:
#             return 0

#         if i in memo:
#             return memo[i]

#         curr = max(recur(i-2)+nums[i], recur(i-1))
#         memo[i] = curr

#         return curr

#     return recur(N-1)

##########################

def rob(self, nums: List[int]) -> int:
	N = len(nums)
	minus2 = 0
	minus1 = 0

	for num in nums:
		curr = max(minus2+num, minus1)
		minus2 = minus1
		minus1 = curr

	return max(minus1, minus2)

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
## [House Robber II (213)](https://leetcode.com/problems/house-robber-ii/)
###### *09/09/2023*

###### Psuedo Code
``` 
# house robber but first and last are connected
# we can disconnect the circle by ignoring one of the houses, take the max of two house robbers ignoring different adjacent houses for each
```

###### Python Solution
```python
def rob(self, nums: List[int]) -> int:
	N = len(nums)

	if N == 1:
		return nums[0]

	first_run = self.houseRobber(nums[:N-1])
	second_run = self.houseRobber(nums[1:N])

	return max(first_run, second_run)
	

def houseRobber(self, nums: List[int]) -> int:
	N = len(nums)
	minus2 = 0
	minus1 = 0

	for i, num in enumerate(nums):
		curr = max(minus2 + num, minus1)
		minus2 = minus1
		minus1 = curr
	
	return max(minus1, minus2)
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
## [Longest Palindromic Substring (5)](https://leetcode.com/problems/longest-palindromic-substring/description/)
###### *09/11/2023*

###### Psuedo Code
``` 
# brute force: find every substring with two forloops, call isPalindrome and update accordingly
# optimized: dp, for every letter we add the longest palidrome is either the existing one or a new palindrome created with the new letter, for each character need to check all odd and even substrings in this way
# optimal: manacher's algorithm. 
```

###### Python Solution
```python
def longestPalindrome(self, s):
	N = len(s)
	max_substr = []

	for i in range(N):
		odd = self.longest(s, i, i, [])
		odd_len = len(odd)
		even = self.longest(s, i, i+1, [])
		even_len = len(even)

		if odd_len > even_len and odd_len > len(max_substr):
			max_substr = odd
		if even_len > odd_len and even_len > len(max_substr):
			max_substr = even

	return max_substr

def longest(self, s, start, end, curr):
	if start < 0 or end > len(s)-1 or s[start] != s[end]:
		return curr

	curr = s[start:end+1]

	return self.longest(s, start-1, end+1, curr)
```

###### Runtime Complexity
```
O(n^2)
```

###### Space Complexity
```
O(n) could be improved by doing iterate expansions
```


---
## [Palindromic Substrings (647)](https://leetcode.com/problems/palindromic-substrings/description/)
###### *09/12/2023*

###### Psuedo Code
``` 
# brute force: calculate all substrings, call isPalidrome on each O(N^3)
# optimize: iterate through s, for each letter, expand outwards to check odd and even palidromes
```

###### Python Solution
```python
def countSubstrings(self, s: str) -> int:
	if not s:
		return 0

	N = len(s)
	count = 0

	# recursive helper
	def expand(start, end):
		nonlocal count

		# base case
		if (start < 0) or (start >= N) or (end >= N) or (s[start] != s[end]):
			return count

		# recursive steps
		count += 1
		return expand(start-1, end+1)

	for i in range(N):
		expand(i, i) # odds
		expand(i, i+1) # evens

	return count
```

###### Runtime Complexity
```
O(n^2)
```

###### Space Complexity
```
O(n)
```


---
## [Decode Ways (91)](https://leetcode.com/problems/decode-ways/description)
###### *12/25/2023*

###### Psuedo Code
``` 
# brute force: break up into all possible ways to group into 1s or 2s and count valid

# dp build up to the solution
```

###### Python Solution
```python
def numDecodings(self, s: str) -> int:
	N = len(s)
	dp = [1] * N

	if N == 0 or s[0] == '0':
		return 0

	for i in range(1, N):
		curr = 0

		# if valid to take as 1 digit
		if s[i] != '0':
			curr += dp[i-1]
		
		# if valid to take as 2 digit
		two_digit = int(s[i-1:i+1])
		if 10 <= two_digit <= 26:
			curr += dp[i-2]

		dp[i] = curr

	return dp[N-1]
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
## [Number of Dice Rolls With Target Sum (1155)](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/)
###### *12/26/2023*

###### Psuedo Code
``` 
# brute force: roll every combination, count the ones that add to target
# optimized: recur + memo
# 1 -> num of ways for 1,6,6
# 2 -> num of ways for 1,6,5
# 3 -> num of ways for 1,6,4
# ...
# base case: once n = 1, there is 1 way iff 1 <= target <= k
```

###### Python Solution
```python
def numRollsToTarget(self, n: int, k: int, target: int) -> int:
	if target > k*n or target < n:
		return 0

	memo = {}

	def recur(n, target):
		curr_ways = 0
		key = (n, target)

		# base case
		if n == 1:
			return 1 if 1 <= target <= k else 0

		# memo
		if key in memo:
			return memo[key]

		# recursive step
		for i in range(1, k+1): 
			curr_ways += recur(n-1, target-i)

		memo[key] = curr_ways 
		return memo[key]

	return recur(n, target) % (10**9 + 7)
```

###### Runtime Complexity
```
O(n * k * target)
```

###### Space Complexity
```
O(n * target)
```


---