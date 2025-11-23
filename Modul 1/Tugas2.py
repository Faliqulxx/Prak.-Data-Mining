mata_kuliah = (
    {"Aljabar Linier": 85},
    {"Struktur Data": 78},
    {"Pemrograman Web": 90},
    {"Kecerdasan Buatan": None},  # Nilai kosong
    {"Jaringan Komputer": 70},
    {"Basis Data": 82},
    {"Analisis Algoritma": None},  # Nilai kosong
    {"Sistem Operasi": 88},
    {"Penggalian Data": None},  # Nilai kosong
    {"Kriptografi": 95}
)

mata_kuliah_bersih = [mk for mk in mata_kuliah if list(mk.values())[0] is not None]

jumlah_tersisa = len(mata_kuliah_bersih)

print("=" * 50)
print("      MATA KULIAH SETELAH PENGHAPUSAN NILAI KOSONG      ")
print("=" * 50)
print("{:<25} {:<10}".format("Mata Kuliah", "Nilai"))
print("-" * 40)
for mk in mata_kuliah_bersih:
    for nama, nilai in mk.items():
        print("{:<25} {:<10}".format(nama, nilai))
print("\nJumlah mata kuliah setelah penghapusan:", jumlah_tersisa)
print("=" * 50, "\n")

mata_kuliah_urut = sorted(mata_kuliah_bersih, key=lambda mk: list(mk.values())[0])

print("=" * 50)
print("      MATA KULIAH SETELAH PENGURUTAN ASCENDING      ")
print("=" * 50)
print("{:<25} {:<10}".format("Mata Kuliah", "Nilai"))
print("-" * 40)
for mk in mata_kuliah_urut:
    for nama, nilai in mk.items():
        print("{:<25} {:<10}".format(nama, nilai))
print("=" * 50, "\n")

mata_kuliah_tertinggi = max(mata_kuliah_urut, key=lambda mk: list(mk.values())[0])

total_nilai = sum(list(mk.values())[0] for mk in mata_kuliah_urut)
rata_rata = total_nilai / jumlah_tersisa

print("=" * 50)
print("     ANALISIS NILAI MATA KULIAH     ")
print("=" * 50)

print("\nMata kuliah dengan nilai tertinggi:")
for nama, nilai in mata_kuliah_tertinggi.items():
    print(f"- {nama}: {nilai}")

print("\nRata-rata nilai mata kuliah: {:.2f}".format(rata_rata))
print("=" * 50)
