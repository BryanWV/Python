#Linear Search algorithm
#Time complexity o(n)
def linear_search(list,element):
	for i in range(len(list)):
		if list[i] == element:
			return i
	return -1

#Linear search
numbers = (64,34,26,346,46,22,90,24,57,21,21) #This can be a tuple(), list[] or set{}
element_to_search = 22
index=linear_search(numbers, element_to_search)
if index != -1:
	print(f"The element {element_to_search} is found in the index {index}.")
else:
	print(f"The element {element_to_search} cannot be found in the list")
