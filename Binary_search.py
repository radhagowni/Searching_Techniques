size=int(input("Enter the size of the array:"))
print("Enter array elements in sorted manner: ")
l=list(map(int,input().split()))
k=int(input("Enter the element to be searched in given array: "))
low=0
high=size-1
idx=-1
while(low<=high):
    mid=(low+high)//2
    if l[mid]==k:
        idx=mid
        break
    elif l[mid]<k:
        low=mid+1 
    else:
        high=mid-1
if idx!=-1:
    print("The element is found at index: ",idx)
else:
    print("Element ",k," is not found in the given array.")