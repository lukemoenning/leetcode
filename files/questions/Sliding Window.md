- [ ] Done with help 
- [x] Done on own

- [x] [[Sliding Window#[Best Time to Buy and Sell Stock (121)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/) |Best Time to Buy and Sell Stock - 07/14/2023]]



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