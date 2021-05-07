"""
given an array of integers return the indices of the two numbers that add up to a given target

Questions
1. will there be duplicates in the array ? no
2. Can the array be empty ? yes
3. are all numbers positive ? yes
4. will there always be a solution ? no
5. what to return if there are no solution ? return Null
6. can there be multiple pairs that add up to target ? No only one pair
"""

def two_sum(array, target):
    hash_map = {}
    for i, num in enumerate(array):
        if target-num in hash_map:
            return [hash_map[target-num], i]
        else:
            hash_map[num] = i


array = [ 1, 3, 2, 9, 4]
target = 11
print(two_sum(array, target))