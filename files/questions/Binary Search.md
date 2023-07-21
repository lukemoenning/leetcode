- [ ] [[Binary Search#[Binary Search (704)](https://leetcode.com/problems/binary-search/description/) |Binary Search - 07/17/2023]]
- [ ] [[Binary Search#[Search a 2D Matrix (74)](https://leetcode.com/problems/search-a-2d-matrix/description/) |Search a 2D Matrix - 07/19/2023]]
- [ ] [[Binary Search#[Koko Eating Bananas (875)](https://leetcode.com/problems/koko-eating-bananas/description/) |Koko Eating Bananas - 07/20/2023]]


---
## [Binary Search (704)](https://leetcode.com/problems/binary-search/description/)
###### *07/17/2023*

###### Psuedo Code
``` 
# check the middle, recurse either left or right
```

###### Python Solution
```python
def search(self, nums: List[int], target: int) -> int:
	return self.bin(nums, 0, len(nums)-1, target)

def bin(self, nums: List[int], left: int, right: int, target: int) -> int:
	if left > right:
		return -1
	mid = left + ((right - left) // 2)

	if nums[mid] == target:
		return mid
	elif nums[mid] > target:
		return self.bin(nums, left, mid-1, target)
	else:
		return self.bin(nums, mid+1, right, target)
```

###### Runtime Complexity
```
O(logn)
```

###### Space Complexity
```
O(logn)
```

---
## [Search a 2D Matrix (74)](https://leetcode.com/problems/search-a-2d-matrix/description/)
###### *07/19/2023*

###### Psuedo Code
``` 
# if we could merge the arrays, could perform binary search
# we can pretend they are combined by doing calculations to find right pointer and middle
```

###### Python Solution
```python
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
	m = len(matrix) # rows
	n = len(matrix[0]) # cols
	left = 0
	right = n*m - 1

	while left <= right: 
		mid = (left + right) // 2
		r = mid // n
		c = mid % n
		print(mid, r, c)
		if matrix[r][c] == target:
			return True
		elif matrix[r][c] > target:
			right = mid - 1
		else:
			left = mid + 1
		
	return False
```

###### Runtime Complexity
```
O(log(nm))
```

###### Space Complexity
```
O(1)
```

---
## [Koko Eating Bananas (875)](https://leetcode.com/problems/koko-eating-bananas/description/)
###### *07/20/2023*

###### Psuedo Code
``` 
# start with a speed of 1 bananas per hour, build up until we find one that works in h hours
# we can optimize this solution by performing a binary search to find the correct speed
# we know that if it takes > h hours to eat the all the bananas we are too slow < h hours we are too fast
# the minimum number of bananas you can eat is 1 and maximum we can benefit from is max(piles) as we can only eat from 1 pile per hour
```

###### Python Solution
```python
def minEatingSpeed(self, piles: List[int], h: int) -> int:
	left, right = 1, max(piles)
	
	while left < right:
		speed = (left + right) // 2

		# iterate through piles and find h for this hypothetical speed
		curr_h = 0
		for bananas in piles:
			hours_for_pile = ceil(bananas / speed)
			curr_h += hours_for_pile
		
		# binary search
		if curr_h > h:
			left = speed + 1
		else: 
			right = speed 

	return right
```

###### Runtime Complexity
```
O(m*logn) where m is max(piles) and n is len(piles)
```

###### Space Complexity
```
O(1)
```


---