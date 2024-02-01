- [ ] Done with help 
- [x] Done on own

- [x] [[Sliding Window#[Best Time to Buy and Sell Stock (121)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/) |Best Time to Buy and Sell Stock - 07/14/2023]]
- [x] [[Sliding Window#[Divide Array into Arrays with Max Difference (2966)](https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/) |Divide Array into Arrays with Max Difference - 01/31/2024]]



---
## [Best Time to Buy and Sell Stock (121)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/) 
###### *07/14/2023*

###### Psuedo Code
``` 
# initialize max_profit and min_price
# iterate through list, update min_price and max_profit as needed
# return max_profit
```

###### Python Solution
```python
def maxProfit(self, prices: List[int]) -> int:
	max_profit = 0
	min_price = math.inf
	for price in prices:
		min_price = min(min_price, price)
		max_profit = max(max_profit, price - min_price)
	return max_profit
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
## [Divide Array into Arrays with Max Difference (2966)](https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/)
###### *01/31/2024*

###### Psuedo Code
``` 
# sort the array, start pulling out three at a time, if we break the condition return empty
```

###### Python Solution
```python
def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
	N = len(nums)
	res = []

	if N%3 != 0:
		return res

	nums.sort()
	i = 0
	while i < N:
		curr_arr = []
		curr_min = nums[i]
		for j in range(i,i+3):
			if nums[j] - curr_min <= k:
				curr_arr.append(nums[j])
			else:
				return []
		res.append(curr_arr)
		i += 3

	return res
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