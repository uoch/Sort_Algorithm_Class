# Sort_Algorithm_Class
SortMethods Class
The sortmethods class provides various sorting algorithms to sort an array of elements in either ascending or descending order.

Installation
No installation is required to use the sortmethods class. Simply copy and paste the class definition into your Python script or import it from your module.

Usage
Create an instance of the sortmethods class by passing an array of elements as an argument to the constructor.

arr = [64, 34, 25, 12, 22, 11, 90]
sort_obj = sortmethods(arr)
You can then use any of the available sorting methods to sort the array:

# Bubble Sort
sort_obj.bubble_sort(ascending=True)

# Insertion Sort
sort_obj.insertion_sort(ascending=True)

# Selection Sort
sort_obj.selection_sort(ascending=True)

# Quick Sort
sort_obj.quick_sort(ascending=True)

# Shell Sort with Knuth Sequence
sort_obj.shell_sort(ascending=True)

# Cocktail Shaker Sort
sort_obj.cocktail_shaker_sort(ascending=True)

# Counting Sort
sort_obj.counting_sort(ascending=True)

# Merge Sort
sort_obj.merge_sort(ascending=True)

# Heap Sort
sort_obj.heap_sort(ascending=True)

# Radix Sort
sort_obj.radix_sort(ascending=True)

# Bitonic Sort
sort_obj.bitonic_sort(ascending=True)
The sorted array can be accessed using the array attribute of the class instance:
python
Copy code
sorted_array = sort_obj.array
By default, the sorting order is ascending, but you can set it to descending by passing False as an argument to the sorting methods:
python
Copy code
sort_obj.bubble_sort(ascending=False)
Example
python
Copy code
# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
sort_obj = sortmethods(arr)

