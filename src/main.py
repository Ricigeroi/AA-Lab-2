import random
import time
import threading
import matplotlib.pyplot as plt

# Size of arrays
small_n = 1000
medium_n = 10000
large_n = 100000

# Partially sorted %
part_n = 0.2

# Generate small, medium, and large arrays
large_array = [random.randint(-10000, 10000) for _ in range(large_n)]
small_array = large_array[:small_n]
medium_array = large_array[:medium_n]

# Generate arrays that are already sorted, partially sorted, or completely unsorted
sorted_array = sorted(large_array.copy())
partially_sorted_array = sorted(large_array[:round(large_n * part_n)]) + large_array[round(large_n * part_n):]
unsorted_array = large_array.copy()


def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n - 1):
        # optimization
        swapped = False
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # if no swaps happened => array already sorted
        if not swapped:
            break
    return arr


def merge_sort(arr):
    # Base case: if the array has only one element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Recursive case: divide the array into two halves and sort each half
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

    return arr


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # If left child is larger than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[largest] < arr[right]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Recursively heapify the affected subtree
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # base case

    pivot = arr[len(arr) // 2]  # choose pivot element
    left = [x for x in arr if x < pivot]  # elements less than pivot
    middle = [x for x in arr if x == pivot]  # elements equal to pivot
    right = [x for x in arr if x > pivot]  # elements greater than pivot

    # recursively sort the left and right subarrays
    return quick_sort(left) + middle + quick_sort(right)


def sleep_sort(numbers):
    sorted_arr = []

    def print_number(number):
        time.sleep(number / 1000)
        sorted_arr.append(number)

    threads = []
    for number in numbers:
        thread = threading.Thread(target=print_number, args=(number,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    return sorted_arr


# Function to time the execution of a sorting function on a given array
def time_sort(sort_fn, arr):
    start_time = time.time()
    sort_fn(arr)
    end_time = time.time()
    return end_time - start_time


def get_time(sort_fn):
    return [
        time_sort(sort_fn, small_array.copy()),
        time_sort(sort_fn, medium_array.copy()),
        time_sort(sort_fn, large_array.copy()),
        time_sort(sort_fn, sorted_array.copy()),
        time_sort(sort_fn, partially_sorted_array.copy())
    ]


# getting results
bubble_time = [time_sort(bubble_sort, small_array), None, None, time_sort(bubble_sort, sorted_array), None]
merge_time = get_time(merge_sort)
heap_time = get_time(heap_sort)
quick_time = get_time(quick_sort)

# print times
print("Bubble sort:", bubble_time)
print("Merge sort:", merge_time)
print("Heap sort:", heap_time)
print("Quick sort:", quick_time)

algorithms = ("Bubble Sort", "Merge Sort", "Heap Sort", "Quick Sort")
result = {
    'Small array': (bubble_time[0], merge_time[0], heap_time[0], quick_time[0]),
    'Medium array': (merge_time[1], heap_time[1], quick_time[1]),
    'Large array': (merge_time[2], heap_time[2], quick_time[2]),
    'Sorted array': (bubble_time[3], merge_time[3], heap_time[3], quick_time[3]),
    'Partially-sorted array': (merge_time[4], heap_time[4], quick_time[4])
}

# Create a single plot with five subplots
fig, axs = plt.subplots(3, 2)

# Plot the data on each subplot
axs[0][0].set_title("Small array of " + str(small_n))
axs[0][0].set_xlabel("Type of algorithm")
axs[0][0].set_ylabel("Time (s)")
axs[0][0].bar(algorithms, result['Small array'])

axs[0][1].set_title("Medium array of " + str(medium_n))
axs[0][1].set_xlabel("Type of algorithm")
axs[0][1].set_ylabel("Time (s)")
axs[0][1].bar(algorithms[1:], result['Medium array'])

axs[1][0].set_title("Large array of " + str(large_n))
axs[1][0].set_xlabel("Type of algorithm")
axs[1][0].set_ylabel("Time (s)")
axs[1][0].bar(algorithms[1:], result['Large array'])

axs[1][1].set_title("Sorted array")
axs[1][1].set_xlabel("Type of algorithm")
axs[1][1].set_ylabel("Time (s)")
axs[1][1].bar(algorithms, result['Sorted array'])

axs[2][0].set_title("Partially-sorted array with % = " + str(part_n))
axs[2][0].set_xlabel("Type of algorithm")
axs[2][0].set_ylabel("Time (s)")
axs[2][0].bar(algorithms[1:], result['Partially-sorted array'])

# Bubble sort
sort_times = []
sort_n = []
for n in range(0, 2001, 100):
    arr = large_array[:n]
    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()
    sort_time = end_time - start_time
    sort_n.append(n)
    sort_times.append(sort_time)

# Plot the results
axs[2][1].plot(sort_n, sort_times)
axs[2][1].set_xlabel('Array Size')
axs[2][1].set_ylabel('Time (seconds)')
axs[2][1].set_title('Bubble Sort Time Complexity')
axs[2][1].grid()
# Adjust the layout of the subplots
fig.tight_layout()

# Show the plot
plt.show()
