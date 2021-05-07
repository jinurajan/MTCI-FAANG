"""
given an array of integers representing an elavation map where the width of the each bar is 1,
return how much rainwater can be trapped

1. will there be negative integers ?
2. can we consider the left and right boundary as walls ?
"""


def trap_rain_water(height):
    # brute force
    total_water = 0
    for i in range(len(height)):
        max_left = 0
        max_right=0
        left_p=i
        right_p = i
        while left_p >= 0:
            max_left = max(height[left_p], max_left)
            left_p -= 1
        while right_p < len(height):
            max_right = max(max_right, height[right_p])
            right_p += 1

        current_water = min(max_left, max_right) - height[i]
        total_water += current_water if current_water > 0 else 0

    return total_water


def trap_rain_water_1(height):
    total_water = 0
    n = len(height)
    max_left_array = [0 for i in range(n)]
    max_right_array = [0 for i in range(n)]
    max_left = height[0]
    max_right = height[-1]
    for i in range(n):
        max_left = max(max_left, height[i])
        max_right = max(max_right, height[n-1-i])
        max_left_array[i] = max_left
        max_right_array[n-1-i] = max_right
    print(max_left_array, max_right_array)

    for i in range(n):
        min_height = min(max_left_array[i], max_right_array[i])
        current = min_height - height[i]
        total_water +=  current if current > 0 else 0
    return total_water


def trap_rain_water_2(height):
    total_water = 0
    n = len(height)
    max_array = [[0,0] for i in range(n)]
    max_left = height[0]
    max_right = height[-1]
    for i in range(n):
        max_left = max(max_left, height[i])
        max_right = max(max_right, height[n - 1 - i])
        max_array[i][0] = max_left
        max_array[n - 1 - i][1] = max_right

    for i in range(n):
        min_height = min(max_array[i][0], max_array[i][1])
        current = min_height - height[i]
        total_water += current if current > 0 else 0
    return total_water

def trap_rain_water_3(height):
    left = 0
    right = len(height)-1
    left_max = 0
    right_max = 0
    ans = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            ans += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            ans += right_max - height[right]
            right -= 1
    return ans


heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap_rain_water(heights))
print(trap_rain_water_1(heights))
print(trap_rain_water_2(heights))
print(trap_rain_water_3(heights))