def partition(arr,l,h):
	pivot=arr[l]
	i=l+1
	j=h-1
	while(True):
		while(i<=j and arr[i]<=pivot):
			i=i+1
		while(i<=j and arr[j]>=pivot):
			j=j-1
		if(i<=j):
			arr[i],arr[j]=arr[j],arr[i]
		else:
			arr[l],arr[j]=arr[j],arr[l]
			return j

def quicksort(arr,l,h):
	if(l<h):
		j=partition(arr,l,h)
		quicksort(arr,l,j)
		quicksort(arr,j+1,h)

arr=[3,9,6,1,4,17,2,76,43,7]
n=len(arr)
quicksort(arr,0,n)
print(arr)
			
