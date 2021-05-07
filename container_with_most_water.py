"""
You are given an array of positive integers where each integer represents the height of a vertical line on a chart.
find two lines which together with the x axis forms a container that would hold the greatest amount of water.
return the area of the water it would hold

questions:

1. does the thickness of the lines affect the area ?
2. can we include the left and right sides of the graph count as wall ?
"""


def container_with_most_water(array):
    left = 0
    right = len(array)-1
    max_area = 0
    while left < right:
        min_val = min(array[left], array[right])
        max_area = max(max_area, min_val*(right-left))
        if min_val == array[left]:
            left += 1
        else:
            right -= 1
    return max_area

array = [1, 7, 2, 9, 3]
print(container_with_most_water(array))