import random

def operasi_list(lst):
    print("List awal:", lst)
    
    for _ in range(10):
        if random.choice([True, False]):
            lst.append(random.randint(0, 100))  
        else:
            lst.append(round(random.uniform(0, 100), 2)) 
    print("List setelah menambahkan 10 elemen acak:", lst)
    
    lst = [lst[i] for i in range(len(lst)) if i % 2 != 0]
    print("List setelah menghapus elemen di indeks genap:", lst)
    
    lst.reverse()
    print("List setelah membalik urutan elemen:", lst)
    
    if lst:  
        nilai_terbesar = max(lst)
        lst.remove(nilai_terbesar)
        print(f"List setelah menghapus elemen terbesar ({nilai_terbesar}):", lst)
    else:
        print("List kosong, tidak ada elemen yang dihapus.")
    
    lst.sort(reverse=True)
    print("List setelah diurutkan secara descending:", lst)
    
    return lst

contoh_list = []
hasil = operasi_list(contoh_list)
print("Hasil akhir:", hasil)