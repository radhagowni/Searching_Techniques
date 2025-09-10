size=int(input("Enter the size of the array:"))
print("Enter array elements: ")
l=list(map(int,input().split()))
k=int(input("Enter the element to be searched in given array: "))
for i in range(len(l)):
    if l[i]==k:
        idx= i 
        break
else:
        idx=-1
if idx!=-1:
 print("The element is present at index: ",idx)
else:
    print("Element ",k," is not found in the given array.")