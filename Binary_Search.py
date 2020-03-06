def IBinsearch(arr,n,key):
	l=1
	h=n
	while(l<h):
		mid=(l+h)//2
		if(key==arr[mid]):
			return mid
		elif(key<arr[mid]):
			h=mid-1
		else:
			l=mid+1
	return -1

def RBinarysearch(arr,l,h,key):
	if(l==h):
		if(arr[l]==key):
			return l
		else:
			return 0
	else:
		mid=(l+h)//2
		if(key==arr[mid]):
			return mid
		elif(key<arr[mid]):
			return RBinarysearch(arr,l,mid-1,key)
		else:
			return RBinarysearch(arr,mid+1,h,key)
	return -1

	

arr=[3,5,18,20,24,29,40,45]
key=18
result=IBinsearch(arr,len(arr),key)
if result==-1:
	print("The given number Not found")
else:
	print("Iterative: The number {} found at index {} ".format(key,result))

result1=RBinarysearch(arr,0,len(arr)-1,key)
if result1==-1:
	print("The given number Not found")
else:
	print("Recursive: The number {} found at index {} ".format(key,result1))

