def maximum_subarray(list):
    maxsum = list[0]
    cur= list [0]
    
    for i in range(1,len(list)):
        cur = max(cur + list[i], list[i])
        maxsum = max(cur, maxsum)
        
    return maxsum

n=int(input())

arr = list(map(int, input(). split()))
print(maximum_subarray(arr))
        
    