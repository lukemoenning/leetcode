- [ ] [[Binary Search#[Binary Search (704)](https://leetcode.com/problems/binary-search/description/) |Binary Search - 07/17/2023]]



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