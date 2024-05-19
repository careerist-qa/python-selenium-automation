# algo 1!!!!
# def sumofdigits(n):
#    result = 0
#    num = n % 10
#    result = result + num
#    n = n // 10
#    num = n % 10
#    result = result + num
#    n = n // 10
#    result = result + n
#
#
#
# print(result)
#
#
# sumofdigits(521)
#
# def maxnum(n):
#    result = [124, 21, 32]
#    result = max(result)
#    print(result)
#
# maxnum(1)
#
# algo 2!!!!
# def split(n):
#    if len(n) % 2 == 0:
#        split = int(len(n) / 2)
#        c = int(split)
#        h1 = (n[c:])
#        h2 = (n[:c])
#        h3 = ''.join([h1, h2])
#         print(h3)
#    else:
#        split = int(len(n) / 2)
#        c = int(split + 1)
#        h1 = (n[c:])
# #        h2 = (n[:c])
#        h4 = ''.join([h1, h2])
#
#        print(split)
#        print(h1)
#        print(h2)
#        print(h3)
#        print(h4)
#
#
# split('oda') #ado
#
# def unique(n):
#    seen = set()
#    uniq = []
#    for x in n:
#        uniq.append(x)
#        seen.add(x)
#        u = len(uniq)
#        s = len(seen)
#        if u == s:
#            print("True")
#        else: print("False")
#
#
# unique('fuisr')
#
#
# algo 3!!!!
# def arithmetica(num_list):
#     mean = sum(num_list)/len(num_list)
#     num_list = [i for i in num_list if i <= mean]
#     return num_list
#
#
# cat = [1, 3, 5, 6, 4, 10, 2, 3]
# print(arithmetica(cat))
#
#
# def low(n):
#     n.sort()
#     return n[0:2]
#
#
# kat = [198, 3, 4, 9, 10, 9, 2]
# print(low(kat))


#algo 4!!!!
# def even_1st(list):
#     list = (sorted(list, key=lambda x: [x % 2, x]))
#     print(list)
#
#
# o = [7, 9, 3, 5, 6, 4, 10, 3, 2]
# even_1st(o)


def Increment(num):
    str(num)
    for i in num:
        d = 0 + i
        print(d)


f = [1, 8, 9]
Increment(f)
