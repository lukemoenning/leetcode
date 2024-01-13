- [ ] Done with help 
- [x] Done on own

- [x] [[Arrays and Hashing#[Contains Duplicate (217)](https://leetcode.com/problems/contains-duplicate/) |Contains Duplicate - 03/11/2023]]
- [x] [[Arrays and Hashing#[Valid Anagram (242)](https://leetcode.com/problems/valid-anagram/)|Valid Anagram - 03/11/2023]]
- [x] [[Arrays and Hashing#[Two Sum (1)](https://leetcode.com/problems/two-sum/) |Two Sum - 09/09/2022]]
- [x] [[Arrays and Hashing#[Group Anagrams (49)](https://leetcode.com/problems/group-anagrams/description/) |Group Anagram - 03/12/2023]]
- [x] [[Arrays and Hashing#[Top K Frequent Elements (347)](https://leetcode.com/problems/top-k-frequent-elements/description/) |Top K Frequent Elements - 03/15/2023]]
- [x] [[Arrays and Hashing#[Product of Array Except Self (238)]( https://leetcode.com/problems/product-of-array-except-self/description/) |Product of Array Except Self - 03/15/2023]]
- [ ] [[Arrays and Hashing#[Valid Sudoku (36)](https://leetcode.com/problems/valid-sudoku/description/) |Valid Sudoku - 03/24/2023]]
- [ ] [[Arrays and Hashing#[Encode and Decode Strings (271)](https://leetcode.com/problems/encode-and-decode-strings/description/) |Encode and Decode Strings - 04/02/2023]]
- [ ] [[Arrays and Hashing#[Longest Consecutive Sequence (128)](https://leetcode.com/problems/longest-consecutive-sequence/description/) |Longest Consecutive Sequence - 04/09/2023]]
- [x] [[Arrays and Hashing#[Widest Vertical Area Between Two Points Containing No Points (1637)]() |Widest Vertical Area Between Two Points Containing No Points - 12/20/2023]]
- [x] [[Arrays and Hashing#[Maximum Score After Splitting a String (1422)](https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=daily-question&envId=2023-12-22) |Maximum Score After Splitting a String - 12/22/2023]]
- [x] [[Arrays and Hashing#[Path Crossing (1296)](https://leetcode.com/problems/path-crossing/description/) |Path Crossing - 12/22/2023]]
- [ ] [[Arrays and Hashing#[Minimum Changes To Make Alternating Binary String (1758)](https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/) |Minimum Changes To Make Alternating Binary String - 12/24/2023]]
- [x] [[Arrays and Hashing#[Redistribute Characters to Make All Strings Equal (1897)](https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/) |Redistribute Characters to Make All Strings Equal - 12/30/2023]]
- [x] [[Arrays and Hashing#[Largest Substring Between Two Equal Characters (1624)](https://leetcode.com/problems/largest-substring-between-two-equal-characters) |Largest Substring Between Two Equal Characters - 12/31/2023]]
- [x] [[Arrays and Hashing#[Assign Cookies (455)](https://leetcode.com/problems/assign-cookies/) |Assign Cookies - 01/01/2024]]
- [x] [[Arrays and Hashing#[Convert an Array Into a 2D Array With Conditions (2610)](https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/) |Convert an Array Into a 2D Array With Conditions - 01/02/2023]]
- [x] [[Arrays and Hashing#[Number of Laser Beams in a Bank (2125)](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/) |Number of Laser Beams in a Bank - 01/03/2024]]
- [x] [[Arrays and Hashing#[Minimum Number of Operations to Make Array Empty (2870)](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/) |Minimum Number of Operations to Make Array Empty - 01/04/2024]]
- [x] [[Arrays and Hashing#[Number of Good Pairs (1512)](https://leetcode.com/problems/number-of-good-pairs/description/) |Number of Good Pairs - 01/08/2024]]
- [x] [[Arrays and Hashing#[Determine if String Halves are Alike (1704)](https://leetcode.com/problems/determine-if-string-halves-are-alike) |Determine if String Halves are Alike - 01/11/2024]]
- [ ] [[Arrays and Hashing#[Minimum Number of Steps to Make Two Strings Anagram (1347)](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/) |Minimum Number of Steps to Make Two Strings Anagram - 01/12/2024]]



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
```python
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
```python
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
```java
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
```python
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
```python
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
			
			
############
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
	res = []
	tupes = []

	# build counts
	counts = Counter(nums)

	# build tuples
	for key in counts.keys():
		tupes.append((key, counts[key]))

	# sort tuples
	tupes.sort(key = lambda x: x[1], reverse=True)

	# build res
	for i in range(k):
		res.append(tupes[i][0])

	# return res
	return res
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
```python
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
```python
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
```python
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
```python
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
## [Widest Vertical Area Between Two Points Containing No Points (1637)](https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points)
###### *12/20/2023*

###### Psuedo Code
``` 
# sort the list and check adjacent pairs
```

###### Python Solution
```python
def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
	N = len(points)
	sorted_points = sorted(points, key=lambda x: x[0])
	widest_area = 0

	for i in range(1, N):
		x1, y1 = sorted_points[i]
		x0, y0 = sorted_points[i-1]
		current_area = x1 - x0
		widest_area = max(widest_area, current_area)

	return widest_area
```

###### Runtime Complexity
```
O(nlogn)
```

###### Space Complexity
```
O(n)
```


---
## [Maximum Score After Splitting a String (1422)](https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=daily-question&envId=2023-12-22)
###### *12/22/2023*

###### Psuedo Code
``` 
# offset one pass by one to account for how we split the string
# two pass, one from left to count zeros and one from right to count ones
```

###### Python Solution
```python
def maxScore(self, s: str) -> int:
	N = len(s)
	scores = [0] * N
	zeros_from_left = 0
	ones_from_right = 0

	for i in range(N):
		if s[i] == '0':
			zeros_from_left += 1
		scores[i] += zeros_from_left
		
	for i in range(N-1, -1, -1):
		scores[i] += ones_from_right
		if s[i] == '1':
			ones_from_right += 1

	return max(scores[:N-1])
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
## [Path Crossing (1296)](https://leetcode.com/problems/path-crossing/description/)
###### *12/22/2023*

###### Psuedo Code
``` 
# maintain a visited set, for each new action, a, ensure we have not visited where it will take us, a'
```

###### Python Solution
```python
def isPathCrossing(self, path: str) -> bool:
	visited = set()
	x, y = 0, 0
	visited.add((x,y))
	transitions = {
		'N': [0,1],
		'S': [0,-1],
		'E': [1,0],
		'W': [-1,0]
	}

	for a in path:
		dx, dy = transitions[a]
		x += dx
		y += dy
		a_prime = (x,y)
		if a_prime in visited:
			return True
		visited.add(a_prime)

	return False
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
## [Minimum Changes To Make Alternating Binary String (1758)](https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/)
###### *12/24/2023*

###### Psuedo Code
``` 
# brute force: O(n^2) for each char, set it as a center point, count how many other characters we would have to change to make this center point valid, return the count of the minimum char

# optimized: we know there are only two potential outcomes after alternating, starting with 0 or starting with 1, two counters and one pass to find the two potential then return the smaller
```

###### Python Solution
```python
def minOperations(self, s: str) -> int:
	N = len(s)
	minimum = float('inf')

	def count_changes(i, center, min_count):
		count = 0

		# check left
		l_prior = center
		for j in range(i-1, -1, -1):
			if s[j] == l_prior:
				count += 1
				if count >= min_count:
					return min_count
			if l_prior == '1':
				l_prior = '0'
			else:
				l_prior = '1'
	
		# check right
		r_prior = center
		for k in range(i+1, N):
			if s[k] == r_prior:
				count += 1
				if count >= min_count:
					return min_count
			if r_prior == '1':
				r_prior = '0'
			else:
				r_prior = '1'

		return count

		
	for index, char in enumerate(s):
		curr_count = count_changes(index, char, minimum)
		minimum = min(minimum, curr_count)

	return minimum




def minOperations(self, s: str) -> int:
	N = len(s)
	start_0 = 0 # if we start with 0, every even index should be 0
	start_1 = 0 # if we start with 1, every even index should be 1

	for i in range(N):
		if (i%2 == 0 and s[i] != '0') or (i%2 == 1 and s[i] != '1'):
			start_0 += 1

		if (i%2 == 0 and s[i] != '1') or (i%2 == 1 and s[i] != '0'):
			start_1 += 1

	return min(start_0, start_1)
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
## [Redistribute Characters to Make All Strings Equal (1897)](https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/)
###### *12/30/2023*

###### Psuedo Code
``` 
# we just need a multiple of N of every char
```

###### Python Solution
```python
def makeEqual(self, words: List[str]) -> bool:
	N = len(words)
	long_s = ''.join(words)
	counts = Counter(long_s)

	for key in counts:
		if counts[key] % N != 0:
			return False

	return True
```

###### Runtime Complexity
```
O(n*k), n = len(words), k = max([len(w) for w in words])
```

###### Space Complexity
```
O(1), since only 26 potential keys
```


---
## [Largest Substring Between Two Equal Characters (1624)](https://leetcode.com/problems/largest-substring-between-two-equal-characters)
###### *12/31/2023*

###### Psuedo Code
``` 
# looking for the largets diff in indicies between two same chars
# brute force: two loops, check every char
# optiimized: two pass, first to record indicies, second through our data structure to find max dif
```

###### Python Solution
```python
def maxLengthBetweenEqualCharacters(self, s: str) -> int:
	# char: [i_1, i_2]
	mp = {}
	max_dif = -1

	for index, char in enumerate(s):
		if char not in mp:
			mp[char] = [index]
		else:
			mp[char].append(index)

	for key in mp:
		high = mp[key][-1]
		low = mp[key][0]
		max_dif = max(max_dif, high-low-1)

	return max_dif 
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
## [Assign Cookies (455)](https://leetcode.com/problems/assign-cookies/)
###### *01/01/2024*

###### Psuedo Code
``` 
# sort both, only assign cookies that make children content
```

###### Python Solution
```python
def findContentChildren(self, g: List[int], s: List[int]) -> int:
	if not s:
		return 0

	N, M = len(g), len(s)
	child_sorted, cookie_sorted = sorted(g), sorted(s)
	child_index, cookie_index = 0, 0
	content_count = 0

	while child_index < N and cookie_index < M:
		if child_sorted[child_index] <= cookie_sorted[cookie_index]:
			content_count += 1
			child_index += 1
		cookie_index += 1

	return content_count
```

###### Runtime Complexity
```
O(nlogn + mlogm)
```

###### Space Complexity
```
O(n+m)
```


---
## [Convert an Array Into a 2D Array With Conditions (2610)](https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/)
###### *01/02/2023*

###### Psuedo Code
``` 
# use a counter to build separate arrays then join them
```

###### Python Solution
```python
def findMatrix(self, nums: List[int]) -> List[List[int]]:
	if not nums:
		return []

	counts = Counter(nums)
	res = []
	distinct_left = len(counts)

	while distinct_left > 0:
		curr = []
		for key in counts:
			if counts[key] > 0:
				curr.append(key)
				counts[key] -= 1
				if counts[key] == 0:
					distinct_left -= 1
		res.append(curr)
	
	return res
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
## [Number of Laser Beams in a Bank (2125)](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/)
###### *01/03/2024*

###### Psuedo Code
``` 
# multiply the most recently seen row with the current
```

###### Python Solution
```python
def numberOfBeams(self, bank: List[str]) -> int:
	if not bank: 
		return 0

	count = 0
	prev = 0
	for row in bank:
		curr_count = row.count('1')
		if curr_count > 0:
			count += prev * curr_count
			prev = curr_count

	return count
```

###### Runtime Complexity
```
O(n*k), k is the longest str
```

###### Space Complexity
```
O(1)
```


---
## [Minimum Number of Operations to Make Array Empty (2870)](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/)
###### *01/04/2024*

###### Psuedo Code
``` 
# count occurences, then use an equation to calculate total
# if there is 1 occurence, return -1
# if there are 2 or 3, add 1
# 4 or more,  
# 4 -> 2,2
# 5 -> 3,2
# 6 -> 3,3
# 7 -> 3,2,2 
# 8 -> 3,3,2
# 9 -> 3,3,3
# 10 -> 3,3,2,2
# 11 -> 3,3,3,2
# 12 -> 3,3,3,3
# 13 -> 3,3,3,2,2
```

###### Python Solution
```python
def minOperations(self, nums: List[int]) -> int:
	if not nums: 
		return -1

	counts = Counter(nums)
	total = 0
	
	for num in counts:
		curr = counts[num]
		if curr == 1:
			return -1
		elif curr == 2 or curr == 3:
			total += 1
		else:
			weight = ((curr - 4) // 3) + 2
			total += weight

	return total
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
## [Number of Good Pairs (1512)](https://leetcode.com/problems/number-of-good-pairs/description/)
###### *01/08/2024*

###### Psuedo Code
``` 
# seen set
```

###### Python Solution
```python
def numIdenticalPairs(self, nums: List[int]) -> int:
	N = len(nums)
	count = 0
	seen = {} # number: count

	for i in range(N):
		if nums[i] in seen:
			count += seen[nums[i]]
			seen[nums[i]] += 1
		else:
			seen[nums[i]] = 1

	return count
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
## [Determine if String Halves are Alike (1704)](https://leetcode.com/problems/determine-if-string-halves-are-alike)
###### *01/11/2024*

###### Psuedo Code
``` 
# helper to count vowels using Counter
```

###### Python Solution
```python
def halvesAreAlike(self, s: str) -> bool:
	if not s:
		return 0

	N = len(s)
	mid = N//2
	first = self.countVowels(s[:mid])
	second = self.countVowels(s[mid:])

	return first == second


def countVowels(self, s: str) -> int:
	if not s:
		return 0

	vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	counts = Counter(s)
	num = 0

	for vowel in vowels:
		if vowel in counts:
			num += counts[vowel]

	return num
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
## [Minimum Number of Steps to Make Two Strings Anagram (1347)](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/)
###### *01/12/2024*

###### Psuedo Code
``` 
# return N - the count of the values in the union of Counters
```

###### Python Solution
```python
def minSteps(self, s: str, t: str) -> int:
	N = len(s)
	s_counts = Counter(s)
	t_counts = Counter(t)
	
	return N - sum((s_counts&t_counts).values())
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