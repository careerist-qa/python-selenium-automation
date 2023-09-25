def lowest_number(nums: list):
    nums.sort()
    print(nums[0:2])
list = [12, 37, 45, 25, 67, 198, 2, 5]
lowest_number(list)

def invert_list(arr: list):
    inverted_arr = []

    for num in arr:
        inverted_num = -num
        inverted_arr.append(inverted_num)

    return inverted_arr


input_list = [1, 5, -2, 4]
output_list = invert_list(input_list)
print(output_list)


def max_diff(arr: list):
    # Check if the list is empty
    # If it is, return 0 as there's no difference to be calculated
    if len(arr) == 0:
        return 0

# Sort the list in ascending order
    arr.sort()
# After sorting, the smallest element will be at index 0,
# and the largest will be at the last index
# Calculate and return the difference between the largest and smallest elements
    return arr[-1] - arr[0]

# Use indexes of the elements
input_list = [0, 1, 6, 1, 2, 9, 4]
result = max_diff(input_list)
print(result)

def larger_than_neighbors(arr: list):
    # Initialize a list 'result' to store elements larger than both neighbors
    result = []

    # Loop through the list from index 1 to len(arr) - 2.
    # We skip the first and the last elements because they don't have both left and right neighbors.
    for i in range(1, len(arr) - 1):
        # Check if the current element (arr[i]) is greater than both its left neighbor (arr[i - 1])
        # and its right neighbor (arr[i + 1]).
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            result.append(arr[i])  # Append the element to the 'result' list

    return result  # Return the list of elements larger than both neighbors

# Example usage:
input_list = [2, 56, 7, 21, 22, 19, 26]
result_list = larger_than_neighbors(input_list)
print(result_list)

def subtract_min(arr: list):
    # Find the minimum element in the list using the 'min' function and store it in 'min_element'.
    min_element = min(arr)

    # Iterate through the list and subtract 'min_element' from each element.
    for i in range(len(arr)):
        arr[i] -= min_element


input_list = [9, 2, 5, 4, 7, 6, 1]
subtract_min(input_list)
print(input_list)



