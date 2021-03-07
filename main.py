def kuaipai(li,low,high):
    if low < high:
        k = li[low]
        i = low
        j = high
        while i < j:
            while j > i and li[j] > k:
                j -= 1
                pass
            if j > i:
                li[i] = li[j]
                i += 1
                pass
            while j > i and li[i] < k:
                i += 1
                pass
            if j > i:
                li[j] = li[i]
                j -= 1
                pass
        li[i] = k

        kuaipai(li,low,i-1)
        kuaipai(li,i+1,high)
        pass
    pass

li = [2,1,5,1,51,7,3,21,34,354,1,35432,354,4,683,4,68,543,687,85,9]
kuaipai(li,0,len(li)-1)
print(li)
