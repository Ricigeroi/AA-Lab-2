import random
import math

# Size of arrays
small_n = 100
medium_n = 10000
large_n = 10

# Partially sorted %
part_n = 0.5

# Generate small, medium, and large arrays
small_array = [random.randint(-10000, 10000) for _ in range(small_n)]
medium_array = [random.randint(-10000, 10000) for _ in range(medium_n)]
large_array = [random.randint(-10000, 10000) for _ in range(large_n)]

# Generate arrays that are already sorted, partially sorted, or completely unsorted
sorted_array = sorted(large_array)
partially_sorted_array = sorted(large_array[:round(large_n * part_n)]) + large_array[round(large_n * part_n):]
unsorted_array = large_array.copy()


print("Small array:", small_array)
print("Medium array:", medium_array)
print("Large array:", large_array)

print("Sorted array:", sorted_array)
print("Partially sorted array:", partially_sorted_array)
print("Unsorted array:", unsorted_array)
