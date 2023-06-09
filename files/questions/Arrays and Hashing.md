1. [[Arrays and Hashing#[Contains Duplicate (217)](https://leetcode.com/problems/contains-duplicate/) |Contains Duplicate - 03/11/2023]]
2. [[Arrays and Hashing#[Valid Anagram (242)](https://leetcode.com/problems/valid-anagram/)|Valid Anagram - 03/11/2023]]
3. [[Arrays and Hashing#[Two Sum (1)](https://leetcode.com/problems/two-sum/) |Two Sum - 09/09/2022]]
4. [[Arrays and Hashing#[Group Anagrams (49)](https://leetcode.com/problems/group-anagrams/description/) |Group Anagram - 03/12/2023]]
5. [[Arrays and Hashing#[Top K Frequent Elements (347)](https://leetcode.com/problems/top-k-frequent-elements/description/) |Top K Frequent Elements - 03/15/2023]]
6. [[Arrays and Hashing#[Product of Array Except Self (238)]( https://leetcode.com/problems/product-of-array-except-self/description/) |Product of Array Except Self - 03/15/2023]]
7. [[Arrays and Hashing#[Valid Sudoku (36)](https://leetcode.com/problems/valid-sudoku/description/) |Valid Sudoku - 03/24/2023]]
8. [[Arrays and Hashing#[Encode and Decode Strings (271)](https://leetcode.com/problems/encode-and-decode-strings/description/) |Encode and Decode Strings - 04/02/2023]]
9. [[Arrays and Hashing#[Longest Consecutive Sequence (128)](https://leetcode.com/problems/longest-consecutive-sequence/description/) |Longest Consecutive Sequence - 04/09/2023]]



--- 
## [Contains Duplicate (217)](https://leetcode.com/problems/contains-duplicate/)
###### *3/11/23*

###### Psuedo Code
``` 
# iterate through the list

	# if the element is not in a set
	
		# add it
	
	# else
	
		# return true
```

###### Python Solution
```
uniques = set()

for num in nums:

	if num in uniques:

		return True

	else:

		uniques.add(num)

return False
```



---
## [Valid Anagram (242)](https://leetcode.com/problems/valid-anagram/)
###### *3/11/23*

###### Psuedo Code
```
# check lengths match

# iterate through s adding each letter to a dict with the value as the num of appearances

# iterate through t decrementing values in the dict, if a value is decremented that doesnt exist return false
```

###### Python Solution
```
if len(s) != len(t):

	return False


dict = {}

for letter in s:

	if letter in dict:

		dict[letter] = dict[letter] + 1

	else:

		dict[letter] = 1


for letter in t:

	if letter not in dict or dict[letter] is 0:

		return False

	else:

		dict[letter] = dict[letter] - 1


return True
```



---
## [Two Sum (1)](https://leetcode.com/problems/two-sum/)
###### *9/9/22*

###### Psuedo Code
```

```

###### Java Solution
```
public int[] twoSum(int[] nums, int target) {

	int[] indices = new int[2];

	HashMap<Integer, Integer> map = new HashMap<>();

	int complement;

	for (int i = 0; i < nums.length; i++){

		complement = target - nums[i];

		if (map.containsKey(complement)){

			indices[0] = i;

			indices[1] = map.get(complement);

			return indices;
		}

		map.put(nums[i], i);
	}
	
	return indices;
}
```


---
## [Group Anagrams (49)](https://leetcode.com/problems/group-anagrams/description/)
###### *03/12/2023*


###### Psuedo Code
``` 
# initialize an empty dictionary, anagrams

# for each string, str, in strs
	# initialize sorted_string to str sorted alphabetically
	
	# if sorted_string does not exists as a key in anagrams
		# add it as a key
	
	# add str to anagrams[sorted_string]

# return the values of anagrams converted to a list
```

###### Python Solution
```
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

	anagrams = {}

	for str in strs:
		sorted_string = "".join(sorted(str))
		
		if sorted_string not in anagrams:
			anagrams[sorted_string] = []

		anagrams[sorted_string].append(str)

	return list(anagrams.values())
```



---
## [Top K Frequent Elements (347)](https://leetcode.com/problems/top-k-frequent-elements/description/)
###### *03/15/2023*

###### Psuedo Code
``` 
# initialize an empty dictionary, num_appearances

# initialize a list of n empty sets where n is the number length of nums. the set stored at index k in the list will contain the numbers that appear k times

# return the k most numbers starting from the last index of the array
```

###### Python Solution
```
# initialize the bucket sort
bucket_sort = [set() for i in range(len(nums)+1)]

# count the number of appearances for each int in nums
num_appearances = Counter(nums)

# sort each count into its proper bucket
for number, index in num_appearances.items():
	bucket_sort[index].add(number)

# return the k right most indexed items
k_most_frequent = []
for i in range(len(bucket_sort)-1, 0, -1):
	for number in bucket_sort[i]:
		k_most_frequent.append(number)
		if len(k_most_frequent) == k:
			return k_most_frequent
```



---
## [Product of Array Except Self (238)]( https://leetcode.com/problems/product-of-array-except-self/description/)
###### *03/15/2023*

###### Psuedo Code
``` 
# initialize an array of length n set to values 1 where n is the length of nums

# for each index multiple it by the product of the values to its left side

# for each index multiple it by the product of the values to its right side
```

###### Python Solution
```
answer = [1]*len(nums)

product_from_left = 1
for i in range(len(answer)):
	answer[i] *= product_from_left
	product_from_left *= nums[i]

product_from_right = 1
for i in range(len(answer) - 1, -1, -1):
	answer[i] *= product_from_right
	product_from_right *= nums[i]

return answer
```



---
## [Valid Sudoku (36)](https://leetcode.com/problems/valid-sudoku/description/)
###### *03/24/2023*

###### Psuedo Code
``` 
# initialize a list of sets for the rows
# initialize a list of sets for the columns
# initialize a list of sets for the 3x3s

# iterate through the board
	# if the current value is '.'
		# continue
	# if the current value already exists for any of the three cases
		# return false
# return true
```

###### Python Solution
```
N = 9

row_sets = [set() for i in range(N)]
col_sets = [set() for i in range(N)]
square_sets = [set() for i in range(N)]

for row in range(N):
	for col in range(N):
		
		current_value = board[row][col]
		
		if current_value == '.':
			continue
		
		if current_value in row_sets[row]:
			return False
		row_sets[row].add(current_value)
		
		if current_value in col_sets[col]:
			return False
		col_sets[col].add(current_value)
		
		square_index = (row//3) * 3 + (col//3)
		if current_value in square_sets[square_index]:
			return False
		square_sets[square_index].add(current_value)

return True
```



---
## [Encode and Decode Strings (271)](https://leetcode.com/problems/encode-and-decode-strings/description/)
###### *04/02/2023*

###### Psuedo Code
``` 
# Encode words using the following pattern
        # Create a variable of the length for the maximun number of characters per string
        # Append the length of the string, filled with zero so it fits in the maximum, followed by the string itself
```

###### Python Solution
```
max_length = 8

class Codec:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        encoded = ''
        for string in strs: 
            encoded += str(len(string)).zfill(max_length)
            encoded += string
            
        return encoded
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        if len(s) == 0:
            return ''
        
        strs = []
        index = 0
        while index < len(s):
            word_length = int(s[index:index+8])
            index += 8
            strs.append(s[index:index+word_length])
            index += word_length

        return strs
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
## [Longest Consecutive Sequence (128)](https://leetcode.com/problems/longest-consecutive-sequence/description/)
###### *04/09/2023*

###### Psuedo Code
``` 
# Create a set from nums
# Create a variable for the longest
# Iterate through the list of nums
# A number is the start of a sequence if the set does not contain the value before it
	# For each sequence starting number
		# Count the length of that sequence
```

###### Python Solution
```
nums_set = set(nums)
longest = 0

for num in nums:

	if num-1 in nums_set:
		continue

	runner = num+1
	current_length = 1
	while runner in nums_set:
		current_length += 1
		runner += 1

	if current_length > longest:
		longest = current_length

return longest
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