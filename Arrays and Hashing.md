1. [[Arrays and Hashing#[Contains Duplicate (217)](https://leetcode.com/problems/contains-duplicate/) |Contains Duplicate - 03/11/2023]]
2. [[Arrays and Hashing#[Valid Anagram (242)](https://leetcode.com/problems/valid-anagram/)|Valid Anagram - 03/11/2023]]
3. [[Arrays and Hashing#[Two Sum (1)](https://leetcode.com/problems/two-sum/) |Two Sum - 09/09/2022]]
4. [[Arrays and Hashing#[Group Anagrams (49)](https://leetcode.com/problems/group-anagrams/description/) |Group Anagram - 03/12/2023]]
5. [[Arrays and Hashing#[Top K Frequent Elements (347)](https://leetcode.com/problems/top-k-frequent-elements/description/) |Top K Frequent Elements - 03/15/2023]]



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