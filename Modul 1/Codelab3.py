import numpy as np # type: ignore
import pandas as pd # type: ignore

# a. Membuat Series dari dictionary berisi nama produk dan ID produk
produk_dict = {"Tablet": 201, "Headphone": 202, "Smartwatch": 203, "Speaker": 204, "Camera": 205}
produk_series = pd.Series(produk_dict)
print("Series Produk:")
print(produk_series)

# b. Membuat DataFrame dengan 4 kolom dan 5 data
produk_data = {
    "Nama": ["Tablet", "Headphone", "Smartwatch", "Speaker", "Camera"],
    "ID": [201, 202, 203, 204, 205],
    "Harga": [5000000, 700000, 2000000, 1500000, 3500000],
    "Stok": [25, 40, 15, 30, 20]
}
df = pd.DataFrame(produk_data)
print("\nDataFrame Produk:")
print(df)

# c. Menambahkan 1 kolom baru
kategori = ["Gadget", "Aksesoris", "Gadget", "Audio", "Kamera"]
df["Kategori"] = kategori
print("\nDataFrame setelah menambahkan kolom Kategori:")
print(df)

# d. Mengurutkan DataFrame berdasarkan Nama
sorted_df = df.sort_values(by="Nama")
print("\nDataFrame setelah diurutkan berdasarkan Nama:")
print(sorted_df)
