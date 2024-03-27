#Selection sort algorithm
#Time complexity o(n^2)
def selection_sort(list):
    n=len(list)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if list[j] < list[min_index]:
                min_index=j
        list[i],list[min_index] = list[min_index], list[i]

numbers=[34,1,2,45,67,42,86,9,0,99]
selection_sort(numbers)
print(numbers)
