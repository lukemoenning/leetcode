- [ ] [[Two Pointers#[Valid Palindrome (125)](https://leetcode.com/problems/valid-palindrome/description/) |Valid Palindrome - 04/09/2023]]
- [ ] [[Two Pointers#[Two Sum II - Input Array is Sorted (167)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/) ||Two Sum II - 04/16/2023]]
- [ ] [[Two Pointers#[3Sum (15)](https://leetcode.com/problems/3sum/description/) |3Sum - 05/28/2023]]
- [ ] [[Two Pointers#[Container With Most Water (11)](https://leetcode.com/problems/container-with-most-water/description/) |Container With Most Water - 05/30/2023]]
- [ ] [[Two Pointers#[Trapping Rain Water (42)](https://leetcode.com/problems/trapping-rain-water/) |Trapping Rain Water - 07/08/2023]]



___
## [Valid Palindrome (125)](https://leetcode.com/problems/valid-palindrome/description/)
###### *04/09/2023*

###### Psuedo Code
``` 
# Two pointers, left and right, one at the beginning and one at the end
    # While left < right
        # Increment/decrement each pointer until they reach an alphanumeric value
        # If s[left] not s[right]
            # Return false
        # Increment left and decrement right
```

###### Python Solution
```python
def isPalindrome(self, s: str) -> bool:
	left = 0
	right = len(s)-1

	while left < right:
		while not s[left].isalnum() and left<right:
			left+=1
	
		while not s[right].isalnum() and left<right:
			right-=1
	
		if s[left].lower() != s[right].lower():
			return False
	
		left+=1
		right-=1
	
	return True
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
## [Two Sum II - Input Array is Sorted (167)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)
###### *04/16/2023*

###### Psuedo Code
``` 
    # two pointers, one at the start and the other at the end
    # three cases: if the sum of the two 
        # equals the target, return them
        # less than the target, increment left pointer
        # greater than the target, decrement right pointer
```

###### Python Solution
```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
	left_pointer = 0 
	right_pointer = len(numbers)-1
	while left_pointer < right_pointer:
		nums_sum = numbers[left_pointer]+numbers[right_pointer]

		if nums_sum == target:
			return [left_pointer+1, right_pointer+1]
		elif nums_sum < target:
			left_pointer+=1
		else:
			right_pointer-=1
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
## [3Sum (15)](https://leetcode.com/problems/3sum/description/)
###### *05/28/2023*

###### Psuedo Code
``` 
# sort nums
# we can't start use the same value for the first number twice, since values are sorted, check that we dont use two of the same values in a row
# if we have not used the first value, call two sum on the rest of the list
# add triples consitiing of the two twosum values with the first value, in sorted order
```

###### Python Solution
```python
def threeSum(self, nums: List[int]) -> Set[Tuple[int]]:
	nums.sort()
	results = set()
	for index, num in enumerate(nums):
		if index == 0 or nums[index] != nums[index-1]:
			self.two_sum(nums[index], nums[index+1:], results)

	return results

def two_sum(self, num: int, array: List[int], results: Set[Tuple[int]]):
	left, right = 0, len(array)-1
	target = -num
	while left<right:
		sum_of_twos = array[left] + array[right]

		if sum_of_twos == target:
			tup = tuple(sorted([num, array[left], array[right]]))
			results.add(tup)
			left+=1
			right-=1
		if sum_of_twos < target:
			left+=1
		if sum_of_twos > target:
			right-=1
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
## [Container With Most Water (11)](https://leetcode.com/problems/container-with-most-water/description/)
###### *05/30/2023*

###### Psuedo Code
``` 
# we know the further apart the two walls the more water the container holds
# two pointers, one at the beginning and other at end
# use a variable to keep track of max
# move the shorter one in each time to maximize potential capacity
```

###### Python Solution
```python
def maxArea(self, height: List[int]) -> int:
	max_water = 0
	left = 0
	right = len(height) - 1
	while left < right:
		distance = right - left
		shortest_height = min(height[left], height[right])
		water = distance * shortest_height
		if water > max_water:
			max_water = water
		
		# move the shorter wall in
		if height[left]<height[right]:
			left+=1
		else:
			right-=1
			
	return max_water

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
## [Trapping Rain Water (42)](https://leetcode.com/problems/trapping-rain-water/)
###### *07/08/2023*

###### Psuedo Code
``` 
# for any given index, i, the water we can trap at that index is min(max on left, max on right) - height[i]
# using arrays we can store the values of maxLeft and maxRight for every i
# then iterate through the height array and perform the calculation

# we cna optimize this using two pointers, we move the pointer that is less towards the middle
# because we choose the pointer that is less, we just need the max from the direction of the pointer we just moved, at that will be our value for min(max on left, max on right)
```

###### Python Solution
```python
def trap(self, height: List[int]) -> int:
	left = 0
	right = len(height) - 1
	max_left = 0
	max_right = 0
	water_trapped = 0
	
	while left<right:
		if height[left] <= height[right]: 
			if height[left] > max_left:
				max_left = height[left]
			left += 1
			if (max_left - height[left]) > 0:
				water_trapped += (max_left - height[left])
		else: 
			if height[right] > max_right:
				max_right = height[right]
			right -= 1
			if (max_right - height[right]) > 0: 
				water_trapped += (max_right - height[right])
		
	
	return water_trapped
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