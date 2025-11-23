import pandas as pd
from tabulate import tabulate

# Membuat DataFrame
data = {
    'Brand': ['Avoskin', 'G2G', 'Skintific', 'Wardah', 'Emina', 'Somethinc', 'Azarine', 'Lacoco', 'Y.O.U', 'Madame Gie'],
    'Cabang': ['Surabaya', 'Jakarta Pusat', 'Bandung', 'Bandung', 'Jakarta', 'Bandung', 'Surabaya', 'Bandung', 'Jakarta Pusat', 'Surabaya'],
    'Harga (ribu)': [150, 75, 120, 85, 75, 120, 50, 90, 55, 50],
    'Stock': [175, 160, 120, 300, 230, 200, 180, 100, 180, 200],
    'Status': ['Sold', 'Available', 'Available', 'Sold', 'Available', 'Available', 'Available', 'Sold', 'Available', 'Sold']
}

df = pd.DataFrame(data)

# 1. Ringkasan Statistik Deskriptif
statistik_deskriptif = df[['Harga (ribu)', 'Stock']].describe().loc[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']]
print("Ringkasan Statistik Deskriptif:")
print(tabulate(statistik_deskriptif, headers='keys', tablefmt='pretty'))
print("\n")

# 2. Tiga Brand dengan Penghasilan Terbesar
df['Penghasilan'] = df['Harga (ribu)'] * df['Stock']
top_3_brand = df.nlargest(3, 'Penghasilan')[['Brand', 'Penghasilan']].reset_index(drop=True)
print("Tiga Brand dengan Penghasilan Terbesar:")
print(tabulate(top_3_brand, headers='keys', tablefmt='pretty'))
print("\n")

# 3. Pengelompokan Brand Berdasarkan Harga
grouped_by_price = df.groupby('Harga (ribu)')['Brand'].apply(list).reset_index()
print("Pengelompokan Brand Berdasarkan Harga:")
print(tabulate(grouped_by_price, headers='keys', tablefmt='pretty', showindex=False))
print("\n")

# 4. DataFrame dengan Kategori Harga
Q1 = df['Harga (ribu)'].quantile(0.25)
Q3 = df['Harga (ribu)'].quantile(0.75)

def kategori_harga(harga):
    if harga < Q1:
        return 'Murah'
    elif harga > Q3:
        return 'Mahal'
    else:
        return 'Sedang'

df['Kategori Harga'] = df['Harga (ribu)'].apply(kategori_harga)
print("DataFrame dengan Kategori Harga:")
print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))