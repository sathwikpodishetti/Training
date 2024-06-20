nums=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
cost=[5,6,5,4,11,2]
l=cost.copy()
for i in range(1,len(nums)):
    for j in range(0,i):
        if nums[i][0]>=nums[j][1]:
            if l[j]+cost[i]>l[i]:
                l[i]=l[j]+cost[i]
print(max(l))