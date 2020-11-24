# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL: EKSEKUSI BERURUTAN
print('Hello World')
print('by Adri')
print('Tanggal 23 November 2020')
print('============' * 3)

mobil = True
if mobil:
    print("Saya mengendarai mobil")
else:
    print("Saya mengendarai motor")
print('============' * 3)

jumlah_anak = 4
for index_anak in range (1, jumlah_anak+1): #jumlah perulangan = 5-1 =4
    print(f'Halo anak #{index_anak}')
print('============' * 3)

print('\nData Type Array')
anak = ['Adri', 'Jaswan', 'Andri', 'Ghotti', 'Anto']
print('sapa semua anak')
print(anak)

print('menambahkan anak')
anak.append('Lilik')
print(anak)

print('\nsapa anak terakhir')
print(f'Hai {anak[5]}')

print('\nsapa semua anak menggunakan for loop')
for urutan in anak:
    print(f'hai {urutan}')

print('\nsapa semua anak menggunakan for loop ke dua')
for urutan in range (0,len(anak)):
    print(f'Hai  anak ke {urutan + 1} {anak[urutan]}')
