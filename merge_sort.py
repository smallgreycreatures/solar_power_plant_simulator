"""Author=Frans Nordén, Date=2016-12-14"""

def mimic_merge_sort(list_to_sort, list_that_mimic_sort_order):
	"""Sorting algorithm written with inspiration from http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html
	Takes two lists with numbers as input arguments where the first list is sorted in decreasing order. 
	The second list just moves the elements on the same index i as in list 1 to the same index j in the 
	sorted list, it hence mimics the operations of the first list. The algorithm is a recursive divide 
	and conquer algorithm that splits lists into one element lists and then merge those lists. 
	During the merge the lists are sorted which enables a time complexity of O(nlogn).

	IMPORTANT: The algorithm demands that the two lists has the same len, else it throws an exception."""
	if len(list_to_sort) != len(list_that_mimic_sort_order):
		raise IndexError("Lists are not the same length. Mimic merge sort demands that. len(list1)=" + 
			str(len(list_to_sort)) + ", len(list2)=" + str(len(list_that_mimic_sort_order)) +".")

    #print("Splitting ",list_to_sort)
	if len(list_to_sort) > 1:
		mid = len(list_to_sort)//2
		left_half = list_to_sort[:mid]
		right_half = list_to_sort[mid:]

		left_half2 = list_that_mimic_sort_order[:mid]
		right_half2 = list_that_mimic_sort_order[mid:]


		mimic_merge_sort(left_half, left_half2)
		mimic_merge_sort(right_half, right_half2)

		i=0
		j=0
		k=0
		#Compare left and right to pick the biggest element and put in final list
		while i < len(left_half) and j < len(right_half):
			if left_half[i] > right_half[j]:
				list_to_sort[k]=left_half[i]
				list_that_mimic_sort_order[k] = left_half2[i]

				i=i+1
			else:
				list_to_sort[k]=right_half[j]
				list_that_mimic_sort_order[k] = right_half2[j]

				j=j+1
			k=k+1

		while i < len(left_half):
			list_to_sort[k]=left_half[i]
			list_that_mimic_sort_order[k] = left_half2[i]

			i=i+1
			k=k+1

		while j < len(right_half):
			list_to_sort[k]=right_half[j]
			list_that_mimic_sort_order[k] = right_half2[j]
			j=j+1
			k=k+1
    #print("Merging ",list_to_sort)

#list_to_sort = [54,26,93,17,77,31,44,55,20]
#list_two = [1,2,3,4,5,6,7,8,9]
#mimic_merge_sort(list_to_sort, list_two)
#print(list_to_sort)
#print(list_two)

