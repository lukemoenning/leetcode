- [ ] Done with help 
- [x] Done on own

- [ ] [[Binary Search#[Binary Search (704)](https://leetcode.com/problems/binary-search/description/) |Binary Search - 07/17/2023]]
- [ ] [[Binary Search#[Search a 2D Matrix (74)](https://leetcode.com/problems/search-a-2d-matrix/description/) |Search a 2D Matrix - 07/19/2023]]
- [ ] [[Binary Search#[Koko Eating Bananas (875)](https://leetcode.com/problems/koko-eating-bananas/description/) |Koko Eating Bananas - 07/20/2023]]
- [ ] [[Binary Search#[Find Minimum in Rotated Sorted Array (153)](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/) |Find Minimum in Rotated Sorted Array - 07/23/2023]]
- [ ] [[Binary Search#[Search in Rotated Sorted Array (33)](https://leetcode.com/problems/search-in-rotated-sorted-array/description/) |Search in Rotated Sorted Array - 07/25/2023]]
- [ ] [[Binary Search#[Median of Two Sorted Arrays (4)](https://leetcode.com/problems/median-of-two-sorted-arrays/description/) |Median of Two Sorted Arrays - 07/30/2023]]


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
## [Find Minimum in Rotated Sorted Array (153)](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)
###### *07/23/2023*

###### Psuedo Code
``` 
# looking for the place where right < left, binary search to find that
```

###### Python Solution
```python
def findMin(self, nums: List[int]) -> int:
	if len(nums) == 1:
		return nums[0]

	n = len(nums)
	left, right = 0, n - 1

	while left < right:
		mid = (left+right) // 2
		if mid+1 < n and nums[mid] > nums[mid + 1]:
			return nums[mid + 1]
		if mid-1 >= 0 and nums[mid-1] and nums[mid-1] > nums[mid]:
			return nums[mid]
		
		if nums[0] < nums[mid]:
			left = mid + 1
		else:
			 right = mid - 1

	return nums[0]
```

###### Runtime Complexity
```
O(logn)
```

###### Space Complexity
```
O(1)
```


---
## [Search in Rotated Sorted Array (33)](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)
###### *07/25/2023*

###### Psuedo Code
``` 
# modified binary search
# when we split the list in half, at least one of the halves will be sorted
# we can perform a simple check to see if it could be contained in the sorted half
# if it cant be it must either be the mid, in the other half, or not in the list
```

###### Python Solution
```python
def search(self, nums: List[int], target: int) -> int:
	left, right = 0, len(nums) - 1

	while left <= right:
		mid = (left + right) // 2

		if nums[mid] == target:
			return mid
		elif nums[left] <= nums[mid]:
			if nums[left] <= target < nums[mid]:
				right = mid - 1
			else:
				left = mid + 1
		else:
			if nums[mid] < target <= nums[right]:
				left = mid + 1
			else:
				right = mid - 1

	return -1
```

###### Runtime Complexity
```
O(logn)
```

###### Space Complexity
```
O(1)
```


---
## [Median of Two Sorted Arrays (4)](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)
###### *07/30/2023*

###### Psuedo Code
``` 
    # brute force: merge the two arrays and perform binary search
    # improved runtime: four pointers, moving the single largest and single smalled toward the middle each time until you have 1 or 2 left

    # optimized: we can just run a binary search on the smaller of the two lists, and assume our solution is correct
    # this means we can calculate how many elements from the larger array would be in left and how many would be in right. total/2 - number in left in smaller array
    # we can then check if our solution is correct if the max in left is less than the max in right for both arrays
    # a trick to avoid out out bounds errors is to set to neg inf if we index out left and pos inf for right
```

###### Python Solution
```python
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
	# ensure nums1 is lesser length
	if len(nums1) > len(nums2): 
		nums1, nums2 = nums2, nums1

	len1 = len(nums1)
	len2 = len(nums2)
	total_length = len1 + len2
	half_total = total_length // 2

	l, r = 0, len1-1
	
	while True:
		pivot1 = (l+r) // 2
		# adjust for index by 0
		pivot2 = half_total - pivot1 - 2

		if pivot1 >= 0: 
			left1 = nums1[pivot1]
		else:
			left1 = -math.inf
		
		if pivot1+1 < len1:
			right1 = nums1[pivot1 + 1]
		else: 
			right1 = math.inf

		if pivot2 >= 0:
			left2 = nums2[pivot2]
		else: 
			left2 = -math.inf

		if pivot2+1 < len2:
			right2 = nums2[pivot2 + 1]
		else:
			right2 = math.inf

		# if our current pivots are valid
		if left1 <= right2 and left2 <= right1:
			# odd total length
			if total_length % 2 == 1:
				return min(right1, right2)

			# even total length
			else:
				return (max(left1, left2) + min(right1, right2)) / 2
		
		elif left1 > right2:
			r = pivot1 - 1
		else:  
			l = pivot1 + 1

	return 0
```

###### Runtime Complexity
```
O(log(min(n,m)))
```

###### Space Complexity
```
O(1)
```


---