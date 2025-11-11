#binary search to find ceil value
s=int(input())
l=list(map(int,input().split()))
element=int(input())
low=0
ans=-1
high=s-1
while(low<=high):
    mid=(low+high)//2
    if l[mid]==element:
        ans=mid
        break
    elif (l[mid]>element):
        ans=mid
        high=mid-1 
    else:
        low=mid+1
if ans==-1:
    print("No such element is found and there is no ceil value of ",element," in the given array")
else:
   print("The ceil value or element ",element," is found at index ",ans)
