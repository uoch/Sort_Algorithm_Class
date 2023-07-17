def compare(x, y, ascending=True):
    return x > y if ascending else x < y


class sortmethods():
    def __init__(self, array):
        self.array = array

    def bubble_sort(self, ascending=True):
        n = len(self.array)
        for i in range(n):
            # Flag to check if any swaps occurred in this pass
            swapped = False

            # Last i elements are already in place, so we don't need to check them
            for j in range(0, n - i - 1):
                if compare(self.array[j], self.array[j + 1], ascending):
                    # Swap the elements if they are in the wrong order
                    self.array[j], self.array[j +
                        1] = self.array[j + 1], self.array[j]
                    swapped = True

            # If no swaps occurred in this pass, the array is already sorted
            if not swapped:
                break

    def insertion_sort(self, ascending=True):
        n = len(self.array)
        for i in range(1, n):
            key = self.array[i]
            j = i - 1
            while j >= 0 and compare(key, self.array[j], ascending):
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key

    def selection_sort(self, ascending=True):
        n = len(self.array)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if compare(self.array[j], self.array[min_idx], ascending):
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]

    def quick_sort(self, ascending=True):
        self._quick_sort(self.array, 0, len(self.array) - 1, ascending)

    def _quick_sort(self, arr, low, high, ascending):
        if low < high:
            # Partition the array and get the pivot index
            pivot_index = self._partition(arr, low, high, ascending)

            # Recursively sort the two sub-arrays
            self._quick_sort(arr, low, pivot_index - 1, ascending)
            self._quick_sort(arr, pivot_index + 1, high, ascending)

    def _partition(self, arr, low, high, ascending):
        # Choose the pivot element (we can use the first element)
        pivot = arr[low]

        # Initialize left and right pointers
        left = low + 1
        right = high

        done = False
        while not done:
            # Move left pointer to the right until it finds an element greater than the pivot
            while left <= right and compare(arr[left], pivot, ascending):
                left += 1

            # Move right pointer to the left until it finds an element smaller than the pivot
            while right >= left and compare(pivot, arr[right], ascending):
                right -= 1

            # If left and right pointers cross each other, we found the correct position for the pivot
            if left > right:
                done = True
            else:
                # Swap the elements at left and right pointers
                arr[left], arr[right] = arr[right], arr[left]

        # Swap the pivot element with the element at the right pointer (final position of the pivot)
        arr[low], arr[right] = arr[right], arr[low]

        # Return the pivot index
        return right

    def shell_sort(self, ascending=True):
        n = len(self.array)
        gap = 1
        while gap <= n // 3:
            gap = gap * 3 + 1

        while gap > 0:
            for i in range(gap, n):
                temp = self.array[i]
                j = i
                while j >= gap and compare(temp, self.array[j - gap], ascending):
                    self.array[j] = self.array[j - gap]
                    j -= gap
                self.array[j] = temp
            gap = (gap - 1) // 3


    def cocktail_shaker_sort(self, ascending=True):
            start = 0
            end = len(self.array) - 1
            swapped = True

            while swapped:
                swapped = False

                # Pass from left to right
                for i in range(start, end):
                    if compare(self.array[i], self.array[i + 1], ascending):
                        self.array[i], self.array[i +
                            1] = self.array[i + 1], self.array[i]
                        swapped = True

                if not swapped:
                    break

                end -= 1

                # Pass from right to left
                for i in range(end, start, -1):
                    if compare(self.array[i - 1], self.array[i], ascending):
                        self.array[i], self.array[i -
                            1] = self.array[i - 1], self.array[i]
                        swapped = True

                start += 1

    def counting_sort(self, ascending=True):
        max_val = max(self.array)
        min_val = min(self.array)
        range_size = max_val - min_val + 1
        count_arr = [0] * range_size

        for num in self.array:
            count_arr[num - min_val] += 1

        idx = 0
        for i in range(range_size):
            while count_arr[i] > 0:
                self.array[idx] = i + min_val
                idx += 1
                count_arr[i] -= 1

    def merge_sort(self, ascending=True):
        def merge(arr, left, mid, right):
            left_arr = arr[left:mid+1]
            right_arr = arr[mid+1:right+1]
            left_len = len(left_arr)
            right_len = len(right_arr)
            i, j, k = 0, 0, left

            while i < left_len and j < right_len:
                if compare(left_arr[i], right_arr[j], ascending):
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1

            while i < left_len:
                arr[k] = left_arr[i]
                i += 1
                k += 1

            while j < right_len:
                arr[k] = right_arr[j]
                j += 1
                k += 1

        def merge_sort_helper(arr, left, right):
            if left < right:
                mid = (left + right) // 2
                merge_sort_helper(arr, left, mid)
                merge_sort_helper(arr, mid + 1, right)
                merge(arr, left, mid, right)

        merge_sort_helper(self.array, 0, len(self.array) - 1)

    def heap_sort(self, ascending=True):
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and compare(arr[largest], arr[left], ascending):
                largest = left

            if right < n and compare(arr[largest], arr[right], ascending):
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        def build_heap(arr):
            n = len(arr)
            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)

        n = len(self.array)
        build_heap(self.array)

        for i in range(n - 1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            heapify(self.array, i, 0)

    def radix_sort(self, ascending=True):
        max_val = max(self.array)
        exp = 1

        while max_val // exp > 0:
            count_arr = [0] * 10
            output = [0] * len(self.array)

            for num in self.array:
                count_arr[(num // exp) % 10] += 1

            for i in range(1, 10):
                count_arr[i] += count_arr[i - 1]

            for i in range(len(self.array) - 1, -1, -1):
                index = (self.array[i] // exp) % 10
                output[count_arr[index] - 1] = self.array[i]
                count_arr[index] -= 1

            for i in range(len(self.array)):
                self.array[i] = output[i]

            exp *= 10

    def bitonic_sort(self, ascending=True):
        def bitonic_merge(arr, low, cnt, ascending):
            if cnt > 1:
                k = cnt // 2
                for i in range(low, low + k):
                    if compare(arr[i], arr[i + k], ascending):
                        arr[i], arr[i + k] = arr[i + k], arr[i]
                bitonic_merge(arr, low, k, ascending)
                bitonic_merge(arr, low + k, k, ascending)

        def bitonic_sort_helper(arr, low, cnt, ascending):
            if cnt > 1:
                k = cnt // 2
                bitonic_sort_helper(arr, low, k, True)
                bitonic_sort_helper(arr, low + k, k, False)
                bitonic_merge(arr, low, cnt, ascending)

        n = len(self.array)
        bitonic_sort_helper(self.array, 0, n, ascending)