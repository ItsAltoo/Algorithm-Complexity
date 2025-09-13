import json
import time

# Membaca file JSON
with open("data.json", "r") as file:
    data = json.load(file)["data"]


def linear_search(arr, target):
    start_time = time.perf_counter()  # Mulai mengukur waktu

    for i in range(len(arr)):
        if arr[i] == target:
            end_time = time.perf_counter()  # Selesai mengukur waktu
            return {
                "index": i,
                "time": (end_time - start_time) * 1000,
            }  # Konversi ke milliseconds

    end_time = time.perf_counter()  # Selesai mengukur waktu (jika tidak ditemukan)
    return {
        "index": -1,
        "time": (end_time - start_time) * 1000,
    }  # Konversi ke milliseconds


result = linear_search(data, 713)  # Mencari angka yang sama seperti di JavaScript
print(f"Index found: {result['index']}")
print(f"Execution time: {result['time']:.6f} milliseconds")

target = [70, 125, 713, 593, 119, 427, 842, 20, 29, 623];