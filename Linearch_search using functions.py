#linear search using a function
def linear_search(l,size,k):
      for i in range(size):
        if l[i]==k:
           return i 
      return -1
 
size=int(input("Enter the size of the array:"))
print("Enter array elements: ")
l=list(map(int,input().split()))
k=int(input("Enter the element to be searched in given array: "))
idx=linear_search(l,size,k)
if idx!=-1:
 print("The element is present at index: ",idx)
else:
    print("Element ",k," is not found in the given array.")
