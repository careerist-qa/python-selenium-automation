
# Python unpacking

# More examples here:
# https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/

def func(a, b, c):
    print(a)
    print(b)
    print(c)


func(a=1, b=2, c=3)

list_num = [1, 2, 3]

func(list_num)   # func([1,2,3] , , ) => will fail
func(*list_num)  # func(1,2,3) => will unpack the list and work
