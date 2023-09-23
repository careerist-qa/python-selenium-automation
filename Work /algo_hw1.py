def bingo(n: int):
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print('bingo')
        elif i % 3 == 0:
            print('bin')
        elif i % 5 == 0:
            print('go')
        else:
            print(i)

bingo(100)

def sum_numbers(n: int):
    final_sum = 0
    for i in range(1, n + 1):
        final_sum = final_sum+ i
    print(f'The sum of digits 1 to {n} is {final_sum}')

sum_numbers(8)

# level 1 Done

def find_max(a: int, b: int, c: int):
    if a > b and c < a:
        print(a)
    elif b > a and c < b:
        print(b)
    else: print(c)

find_max(14,15, 16)

def leap_year(year: int):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("True")
    else:
        print("False")

leap_year(2024)


# Level 2 Done

def generate_fibonacci_sequence(n: int):
    # Initialize the list with the first two Fibonacci numbers
    fib_sequence = [0, 1]
    # Use a for loop to generate the remaining Fibonacci numbers after the first two
    for i in range(2, n):
        # Calculate the next Fibonacci number using the formula fib_sequence[-1] + fib_sequence[-2]
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        # Append the new Fibonacci number to the list using the append() function
        fib_sequence.append(next_fib)

    print(fib_sequence)

generate_fibonacci_sequence(15)




