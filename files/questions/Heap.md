- [ ] Done with help 
- [x] Done on own

- [ ] [[Heap#[Kth Largest Element in an Array (215)](https://leetcode.com/problems/kth-largest-element-in-an-array/description/) |Kth Largest Element in an Array - 12-20-2023]]



---
## [Kth Largest Element in an Array (215)](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)
###### *12-20-2023*

###### Psuedo Code
``` 
# maintain a heap of size k, containing the k largest elements
```

###### Python Solution
```python
def findKthLargest(self, nums: List[int], k: int) -> int:
	N = len(nums)
	h = nums[:k]
	heapq.heapify(h)

	for i in range(k, N):
		if nums[i] > h[0]:
			heapq.heappop(h)
			heapq.heappush(h, nums[i])

	return h[0]
```

###### Runtime Complexity
```
O(nlogk)
```

###### Space Complexity
```
O(k)
```


---