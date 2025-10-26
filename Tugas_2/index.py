import requests
import json

api = "http://localhost:8000/api/foods"
token = "d660cadfa05383d82263f91f2e6525c9c653114c"

headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}

try:
    res = requests.get(api, headers=headers)

    res.raise_for_status()  # Ini akan menampilkan error jika request gagal (status code 4xx atau 5xx)

    # 4. Jika berhasil, proses datanya (biasanya dalam format JSON)
    data = res.json()
    print("Request Berhasil!")
    # Tampilkan data dengan format yang rapi
    print(json.dumps(data, indent=2))
    print(f"Panjang data: {len(data)}")

except requests.exceptions.HTTPError as errh:
    print(f"Http Error: {errh}")
    # Jika token salah atau tidak valid, Anda akan sering mendapatkan status code 401 atau 403
    if errh.res.status_code == 401:
        print("Error 401: Unauthorized. Pastikan token Anda benar dan valid.")
    elif errh.res.status_code == 403:
        print(
            "Error 403: Forbidden. Anda tidak memiliki izin untuk mengakses resource ini."
        )
except requests.exceptions.RequestException as err:
    print(f"Error Lainnya: {err}")

print("~" * 20)


# Fungsi untuk mendapatkan nilai kalori dari makanan
def get_calories(food_item):
    return food_item["nutrition"]["calories"]


# Algoritma Insertion Sort untuk mengurutkan data berdasarkan kalori tertinggi
def insertion_sort(food_list):
    # Loop melalui setiap makanan mulai dari index 1
    for i in range(1, len(food_list)):
        # Simpan makanan yang sedang kita periksa
        makanan_yang_diperiksa = food_list[i]
        kalori_yang_diperiksa = get_calories(makanan_yang_diperiksa)

        # Mulai bandingkan dengan makanan-makanan sebelumnya
        posisi = i

        # Geser makanan ke kanan selama kalorinya lebih kecil dari yang diperiksa
        while (
            posisi > 0 and get_calories(food_list[posisi - 1]) < kalori_yang_diperiksa
        ):
            food_list[posisi] = food_list[posisi - 1]
            posisi -= 1

        # Masukkan makanan yang diperiksa ke posisi yang tepat
        food_list[posisi] = makanan_yang_diperiksa

    return food_list


# Urutkan data makanan berdasarkan kalori tertinggi
sorted_data = insertion_sort(data)
print("\nData setelah diurutkan berdasarkan kalori tertinggi:")
print(json.dumps(sorted_data, indent=2))
