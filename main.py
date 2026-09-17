import threading
import time


# Merge two sorted parts
def merge(arr, left, mid, right):
    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    arr[left:right + 1] = temp


# Normal Merge Sort
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)


# Multithreaded Merge Sort
def threaded_merge_sort(arr, left, right, depth=0):
    if left < right:
        mid = (left + right) // 2

        # Create threads only for the first few levels
        if depth < 2:
            t1 = threading.Thread(
                target=threaded_merge_sort,
                args=(arr, left, mid, depth + 1)
            )

            t2 = threading.Thread(
                target=threaded_merge_sort,
                args=(arr, mid + 1, right, depth + 1)
            )

            t1.start()
            t2.start()

            t1.join()
            t2.join()

        else:
            merge_sort(arr, left, mid)
            merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)


# ---------------- MAIN PROGRAM ----------------

print("===== MERGE SORT COMPARISON =====")

# User input
n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter the elements separated by space: ").split()))

if len(arr) != n:
    print("Error: Number of elements does not match.")
else:

    # Normal Merge Sort
    normal_arr = arr.copy()

    start_time = time.perf_counter()
    merge_sort(normal_arr, 0, n - 1)
    end_time = time.perf_counter()

    normal_time = end_time - start_time

    # Multithreaded Merge Sort
    threaded_arr = arr.copy()

    start_time = time.perf_counter()
    threaded_merge_sort(threaded_arr, 0, n - 1)
    end_time = time.perf_counter()

    threaded_time = end_time - start_time

    # Output
    print("\nOriginal Array:")
    print(arr)

    print("\nNormal Merge Sort:")
    print(normal_arr)

    print("Time:", normal_time, "seconds")

    print("\nMultithreaded Merge Sort:")
    print(threaded_arr)

    print("Time:", threaded_time, "seconds")

    # Compare performance
    print("\n===== PERFORMANCE COMPARISON =====")

    if normal_time < threaded_time:
        print("Normal Merge Sort is faster for this input.")
    elif threaded_time < normal_time:
        print("Multithreaded Merge Sort is faster for this input.")
    else:
        print("Both sorting methods have similar performance.")

    print("\nTime Complexity:")
    print("Best Case  : O(n log n)")
    print("Worst Case : O(n log n)")