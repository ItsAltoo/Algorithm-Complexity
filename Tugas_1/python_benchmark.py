# python_benchmark.py
import time
import random
import gc


def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


# setup
N = 100_000  # ukuran array
ITER = 10_000  # jumlah pencarian
arr = list(range(N))
random.seed(0)
targets = [random.randint(0, N - 1) for _ in range(ITER)]

# Mencari nilai min dan max dari array
min_val = min(arr)
max_val = max(arr)
min_idx = arr.index(min_val)
max_idx = arr.index(max_val)
print("\nPython :")
print(f"\nNilai terkecil: {min_val} pada index: {min_idx}")
print(f"Nilai terbesar: {max_val} pada index: {max_idx}\n")

# Mengukur waktu pencarian
gc.disable()  # optional: disable GC during measurement

min_time = float("inf")
max_time = float("-inf")
min_target = 0
max_target = 0

# Warm-up
for t in targets[:100]:
    linear_search(arr, t)

# Mencari waktu minimum dan maximum untuk setiap pencarian
for target in targets:
    start_time = time.perf_counter()
    index = linear_search(arr, target)
    end_time = time.perf_counter()
    search_time = end_time - start_time

    if search_time < min_time:
        min_time = search_time
        min_target = target
    if search_time > max_time:
        max_time = search_time
        max_target = target

gc.enable()

print("Pencarian tercepat:")
print(f"Target: {min_target}")
print(f"Waktu: {min_time*1000:.6f} ms")
print(f"Index: {linear_search(arr, min_target)}")

print("\nPencarian terlama:")
print(f"Target: {max_target}")
print(f"Waktu: {max_time*1000:.6f} ms")
print(f"Index: {linear_search(arr, max_target)}")

# Mengukur total waktu untuk semua pencarian
start_total = time.perf_counter()
for target in targets:
    linear_search(arr, target)
end_total = time.perf_counter()

total = end_total - start_total
print(f"\ntotal {total} avg {total/ITER}")
