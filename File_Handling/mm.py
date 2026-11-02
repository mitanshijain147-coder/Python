nums = [3,2,2]
rep = 0
ans = []
for i in nums:
    if nums.count(i)>1:
        rep=i
print(rep)  
n = len(nums)
for j in range (1,n+1):
    ans.append(j)
print(ans)