import random

def bogosort(lst):
    while not is_sorted(lst):
        random.shuffle(lst)
    return lst

def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

# Example usage
lst = [random.randint(-10000, 10000) for _ in range(100)]
sorted_lst = bogosort(lst)
print(sorted_lst)
