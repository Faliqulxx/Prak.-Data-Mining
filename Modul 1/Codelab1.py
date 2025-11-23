data_tuple = [
    (1, 3.14, 'apel', 5),
    (2, 2.71, 'pisang', 3),
    (10, 1.61, 'anggur', 7),
    (8, 4.2, 'jeruk', 6),
    (5, 9.8, 'melon', 2),
    (6, 3.5, 'kiwi', 4),
    (3, 7.1, 'pear', 9),
    (4, 0.9, 'ceri', 8),
    (9, 6.3, 'semongko', 1),
    (7, 5.5, 'mangga', 10),
    (11, 8.4, 'nanas', 12),
    (12, 3.9, 'kates', 11)
]

data_list = [list(tup) for tup in data_tuple]
print("Data List Awal:", data_list)

data_list.insert(10, [13, 4.5, 'kelapa', 15])  
data_list.insert(10, [14, 3.3, 'stoberi', 16])
print("\nData List setelah penambahan:", data_list)

data_list_no_float = [
    [x for x in item if not isinstance(x, float)] for item in data_list
]
print("\nData List tanpa tipe float:", data_list_no_float)

data_list_sorted_desc = sorted(data_list_no_float, reverse=True)
print("\nData List setelah diurutkan descending:", data_list_sorted_desc)
