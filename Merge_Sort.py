def MergeSort(arr):
	print("SPLITTING",arr)
	if(len(arr)>1):
		mid=len(arr)//2
		l=arr[:mid]
		h=arr[mid:]
		
		MergeSort(l)
		MergeSort(h)
		i=j=k=0
		while(i<len(l) and j<len(h)):
			if(l[i]<h[j]):
				arr[k]=l[i]
				i=i+1
			else:
				arr[k]=h[j]
				j=j+1
			k=k+1

		while(i<len(l)):
			arr[k]=l[i]
			k+=1
			i+=1

		while(j<len(h)):
			arr[k]=h[j]
			k+=1
			j+=1
	print("MERGING",arr)

arr=[20,3,40,12,63]
MergeSort(arr)
print(arr)
