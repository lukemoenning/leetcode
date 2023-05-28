1. [[Two Pointers#[Valid Palindrome (125)](https://leetcode.com/problems/valid-palindrome/description/) |Valid Palindrome - 04/09/2023]]
2. [[Two Pointers#[Two Sum II - Input Array is Sorted (167)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/) ||Two Sum II - 04/16/2023]]
3. [[Two Pointers#[3Sum (15)](https://leetcode.com/problems/3sum/description/) |3Sum - 05/28/2023]]



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
```
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
O(N)
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
```
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
O(N)
```

###### Space Complexity
```
O(N)
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
```
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
O(N^2)
```

###### Space Complexity
```
O(N)
```

---