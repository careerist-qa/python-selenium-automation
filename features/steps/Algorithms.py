#def sumofdigits(n):
#    result = 0
#    num = n % 10
#    result = result + num
#    n = n // 10
#    num = n % 10
#    result = result + num
#    n = n // 10
#    result = result + n



# print(result)


#sumofdigits(521)

#def maxnum(n):
#    result = [124, 21, 32]
#    result = max(result)
#    print(result)

#maxnum(1)

#def split(n):
#    if len(n) % 2 == 0:
#        split = int(len(n) / 2)
#        c = int(split)
#        h1 = (n[c:])
#        h2 = (n[:c])
 #       h3 = ''.join([h1, h2])
   #      print(h3)
#    else:
#        split = int(len(n) / 2)
#        c = int(split + 1)
#        h1 = (n[c:])
##        h2 = (n[:c])
#        h4 = ''.join([h1, h2])

#        print(split)
#        print(h1)
 #       print(h2)
#        print(h3)
#        print(h4)


#split('oda') #ado

def unique(n):
    seen = set()
    uniq = []
    for x in n:
        uniq.append(x)
        seen.add(x)
        u = len(uniq)
        s = len(seen)
        if u == s:
            print("True")
        else: print("False")








unique('fuisr')