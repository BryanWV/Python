#Merge sort algorithm
#Divide & Conquer
#Divide the list in smaller lists
#Sort them individually and then combine in sorted list
def merge_sort(list):
    if len(list) <=1:
        return list
    
    mid = len(list) //2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left,right)

def merge(left,right):
    result=[]
    i = j = 0 
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

numbers= [3,1,4,7,54,13,83,9,40,41,44,77]
sorted = merge_sort(numbers)
print(sorted)
