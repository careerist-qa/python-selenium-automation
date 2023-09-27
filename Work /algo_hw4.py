def sum_even_and_product_odd(arr: list):
    # Initialize variables for the sum of even numbers and the product of odd numbers
    sum_even = 0
    product_odd = 1

    for i in arr:
        if i % 2 == 0:
            sum_even += i
        else:
            product_odd *= i

    print(arr)
    print([sum_even, product_odd])

sum_even_and_product_odd([12,11,19,18])

def sum_between_range(arr: list, min_val: int, max_val: int):
    total_sum = 0

    for num in arr:
        if min_val <= num <= max_val:
            total_sum += num

    return total_sum

arr = [3, 4, 6, 5, 11, 9, 7, 6, 9, 5]
min_val = 3
max_val = 7
result = sum_between_range(arr, min_val, max_val)
print(result)

def buy_and_sell_stock(prices: list):
    # Initialize the variable 'maximum' to store the maximum profit, starting at 0
    maximum = 0


    for i in range(len(prices) - 1):

        if prices[i + 1] > prices[i]:
            maximum += prices[i + 1] - prices[i]


    return maximum

prices = [7, 1, 5, 3, 6, 4]
result = buy_and_sell_stock(prices)
print(result)


def plus_one(arr: list):

    arr[-1] += 1

    for i in reversed(range(1, len(arr))):
            if arr[i] != 10:
            break

        arr[i] = 0

        arr[i - 1] += 1

    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)



arr = [1, 2, 9]
plus_one(arr)
print(arr)




