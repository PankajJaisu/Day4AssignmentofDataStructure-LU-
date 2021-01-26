def sort(s,key,l,h):
    while l<=h:
        m=(l+h)//2
        if s[m]==key:
            return m
        elif s[m]>key:
            h=m-1
        else:
            l=m+1
    return -1
s=[int(i) for i in input('Enter values: ').split()]
key=int(input("Enter value to be search:"))
s.sort()
l=0
h=len(s)-1
res=sort(s,key,l,h)
if res==-1:
    print("Element is not Found")
else:
    print("Element is Found at ",res)