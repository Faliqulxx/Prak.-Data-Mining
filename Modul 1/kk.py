import random

def operasi_list(lst):
    print("List awal:", lst)
    
    # Tambahkan 10 elemen numerik int dan float secara acak
    for _ in range(10):
        if random.choice([True, False]):
            lst.append(random.randint(0, 100))  # Menambahkan integer acak
        else:
            lst.append(round(random.uniform(0, 100), 2))  # Menambahkan float acak
    print("List setelah menambahkan 10 elemen acak:", lst)
    
    # Hapus elemen di indeks genap
    lst = [lst[i] for i in range(len(lst)) if i % 2 != 0]
    print("List setelah menghapus elemen di indeks genap:", lst)
    
    # Balik urutan elemen dalam list
    lst.reverse()
    print("List setelah membalik urutan elemen:", lst)
    
    # Hapus elemen dengan nilai terbesar dari list tersebut
    if lst:  # Pastikan list tidak kosong
        nilai_terbesar = max(lst)
        lst.remove(nilai_terbesar)
        print(f"List setelah menghapus elemen terbesar ({nilai_terbesar}):", lst)
    else:
        print("List kosong, tidak ada elemen yang dihapus.")
    
    # Urutkan elemen pada list secara descending
    lst.sort(reverse=True)
    print("List setelah diurutkan secara descending:", lst)
    
    return lst

# Contoh penggunaan
contoh_list = []
hasil = operasi_list(contoh_list)
print("Hasil akhir:", hasil)