ls=[1,3,5,7]
k=5
n=len(ls)
first=0
last=n-1
mid=(first+last)//2

while first<=last:
    if ls[mid]==k:
        print("index", mid)
        break
    elif k<ls[mid]:
        last=mid-1
        mid=(first+last)//2
    elif ls[mid]<k:
        first=mid+1
        mid=(first+last)//2
    else:
        print("Error")
        break
