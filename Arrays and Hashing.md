1. [[Arrays and Hashing#[Contains Duplicate (217)](https://leetcode.com/problems/contains-duplicate/) |Contains Duplicate 3/11/23]]
2. [[Arrays and Hashing#[Valid Anagram (242)](https://leetcode.com/problems/valid-anagram/)|Valid Anagram #242 3/11/23]]
3. [[Arrays and Hashing#[Two Sum (1)](https://leetcode.com/problems/two-sum/) |Two Sum 9/9/22]]



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
