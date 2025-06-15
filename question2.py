# sorting function using the last element as pivot element
def quicksort(arr, left, right, depth=0):
    if left < right:
        pivot_index = partition(arr, left, right, depth)  # partitioning the array and get the pivot index
        quicksort(arr, left, pivot_index - 1, depth + 1)  # sorting the left part
        quicksort(arr, pivot_index + 1, right, depth + 1) # sorting the right part

# function of partitioning the array using the last element as the pivot element
def partition(arr, left, right, depth):
    pivot = arr[right]  # last element as pivot
    i = left - 1  # index for smaller element
    print()
    print(f"{'  ' * depth}Partitioning :" )
    print(f"{'  ' * depth}    {arr[left:right+1]} | Pivot: {pivot}")

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1  # incrementing 
            arr[i], arr[j] = arr[j], arr[i]  # swapping

    arr[i + 1], arr[right] = arr[right], arr[i + 1]  # swapping pivot element to its correct position

    print(f"{'  ' * depth}After partition :")
    print(f"{'  ' * depth}    {arr}")
    return i + 1  # returning the partition index

# sample list of words
words = ["fewer","drest","fuzes","porae","moose","feuar","zoppo","piing","sesey","acted","imino"]

print("\n Initial list:")
print(words)

# Sorting the list using quicksort
quicksort(words, 0, len(words) - 1)

print("\nSorted list:")
print( words)
