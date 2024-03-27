#Insertion sort algorithm
#Time complexity o(n^2)
#Insertion sort is more efficient than bubble sort
#If the list has some sorting
def insertion_sort(list):
    for i in range(1,len(list)):
        key=list[i]
        j=i-1
        while j >=0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key

numbers=[1,2,5,3,9,57,25,91,92,81,90]
insertion_sort(numbers)
print(numbers)
