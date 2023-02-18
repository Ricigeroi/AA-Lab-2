import random
import threading
import time

# Size of arrays
small_n = 100
medium_n = 1000
large_n = 10000

# Partially sorted %
part_n = 0.2

# Generate small, medium, and large arrays
large_array = [random.randint(0, 10000) for _ in range(large_n)]
small_array = large_array[:small_n]
medium_array = large_array[:medium_n]


# Generate arrays that are already sorted, partially sorted, or completely unsorted
sorted_array = sorted(large_array.copy())
partially_sorted_array = sorted(large_array[:round(large_n * part_n)]) + large_array[round(large_n * part_n):]
unsorted_array = large_array.copy()

def sleep_sort(numbers):
    sorted_arr = []
    def print_number(number):
        time.sleep(number)
        sorted_arr.append(number)

    threads = []
    for number in numbers:
        thread = threading.Thread(target=print_number, args=(number,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    return sorted_arr


arr = [random.randint(0, 10) for _ in range(10)]
print(arr)
sor = sleep_sort(arr.copy())
print(sor)