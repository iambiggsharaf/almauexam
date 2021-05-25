a = [
    [50, 50],
    [70, 15, 15],
    [90, 5, 2.5, 2.5],
    [99, 10],
]

def myFunction(arr):
    even = True
    odd = True
    
    for i in range(0, len(arr)):

        if i % 2 == 0:
            cnt = 0
            for j in arr[i]:
                cnt += 1
            if cnt % 2 != 0:
                even = False
            # print(cnt)
        
        else:
            cnt = 0
            for j in arr[i]:
                cnt += 1
            if cnt % 2 == 0:
                odd = False
            # print(cnt)
    
    if even == True and odd == True:
        return True
    else:
        return False

print(myFunction(a))

            