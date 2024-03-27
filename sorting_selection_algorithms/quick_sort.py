#Quick sort algorithm
#Time complexity o(n^2)

def quick_sort(list):
    if len(list) <=1:
        return list
    
    pivot = list[len(list) //2]
    left = [x for x in list if x < pivot]
    mid = [x for x in list if x == pivot]
    right = [x for x in list if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)

numbers = [3,35,12,46,73,90,87,54,77,1,0]
sorted= quick_sort(numbers)
print(sorted)
