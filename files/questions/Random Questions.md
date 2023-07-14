1. [[Random Questions#[Sort Integers by The Number of 1 Bits (1356)](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/) |Sort Integers by The Number of 1 Bits - 07/07/2023]]
2. [[Random Questions#[House Robber (198)](https://leetcode.com/problems/house-robber/description/) |House Robber - 07/09/2023]]
3. [[Random Questions#[Maximum Subarray (53)](https://leetcode.com/problems/maximum-subarray/description/) |Maximum Subarray - 07/13/2023]]
4. [[Random Questions#[Longest Substring Without Repeating Characters (3)](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/) |Longest Substring Without Repeating Characters - 07/13/2023]]



---
## [Sort Integers by The Number of 1 Bits (1356))](Thttps://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/)
###### *07/07/2023*

###### Psuedo Code
``` 
# sort the list in place in ascending order
# sort the list by the count of the "1 bit"
# return the array
```

###### Python Solution
```
def sortByBits(self, arr: List[int]) -> List[int]:
	arr.sort()
	arr = sorted(arr, key=lambda x:bin(x).count('1'))
	return arr
```

###### Runtime Complexity
```
O(nlogn)
```

###### Space Complexity
```
O(1)
```

---
## [House Robber (198)](https://leetcode.com/problems/house-robber/description/)
###### *07/09/2023*

###### Psuedo Code
``` 
# could use memo and recursion to build a tree, for each index we want the max(current + 2back, 1back)

# instead, we can build up to in similiar to fibonacci
```

Python Solution
``` Python
def rob(self, nums: List[int]) -> int:
	nMinus2 = 0
	nMinus1 = 0
	for num in nums:
		current = max(nMinus2 + num, nMinus1)
		nMinus2 = nMinus1
		nMinus1 = current

	return max(nMinus1, nMinus2)
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
## [Maximum Subarray (53)](https://leetcode.com/problems/maximum-subarray/description/)
###### *07/13/2023*

###### Psuedo Code
``` 
# dp, the currentsubarray at the current location is equal to the max(existing_max+current, current)
# iterate through list, update current and max for each value
```

###### Python Solution
```python
def maxSubArray(self, nums: List[int]) -> int:
	max_sub = nums[0]
	current_sub = nums[0]
	for num in nums[1:]:
		current_sub = max(current_sub + num, num)
		max_sub = max(max_sub, current_sub)
	
	return max_sub
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
## [Longest Substring Without Repeating Characters (3)](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)
###### *07/13/2023*

###### Psuedo Code
``` 
# sliding window, keep track of seen
# iterate through the list
# if we have not seen the letter, update max_length
# while the s[i] is in seen, remove it and slide the back half of the window forward
# finally, add s[i] to seen
```

###### Python Solution
```python
def lengthOfLongestSubstring(self, s: str) -> int:
	max_length = 0
	seen = set()
	start = 0
	for i in range(len(s)):
		if s[i] not in seen:
			max_length = max(max_length, i - start + 1)
		while s[i] in seen:
			seen.remove(s[start])
			start += 1
		seen.add(s[i])

	return max_length
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