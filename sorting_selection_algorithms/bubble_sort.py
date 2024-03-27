#Bubble sort algorithm
#It compares pairs of adjacent elements and swaps them
#if they are in the wrong order until the list is sorted
#Time complexity o(n^2)
def bubble_sort(list):
    n=len(list)
    for i in range(n):
            for j in range(0,n-i-1):
                  if list[j]>list[j+1]:
                        list[j],list[j+1]=list[j+1],list[j]

numbers=[64,36,25,43,22,11,90,45,9,7,11,99]
bubble_sort(numbers)
print(numbers)