import sys
import platform

# Menampilkan versi interpreter Python secara detail
print(f"Versi Python: {sys.version}")

# Menampilkan informasi OS yang lebih lengkap
print(f"Sistem Operasi: {platform.platform()}")

# Menampilkan informasi engine
print(f"Engine: {platform.python_implementation()}")

# Output Contoh:
# Versi Python: 3.11.4 (main, Jun  7 2023, 10:13:09) [GCC 12.2.0]
# Sistem Operasi: Linux-6.1.0-13-amd64-x86_64-with-glibc2.36