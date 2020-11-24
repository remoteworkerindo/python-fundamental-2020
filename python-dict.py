"""
Tipe data dictionary sekedar menghubungkan antara KEY dan Value
KVP = Key Value Pair
dictionary = Kamus
"""

kamus_ind_eng = {'anak': 'son', 'ayah': 'father', 'ibu': 'mother', 'istri': 'wife', 'uncle': 'om'}
print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])
print(kamus_ind_eng['istri'])

print('Data ini dikirimkan oleh server gojek untuk mengrimkan info driver ke pemakai aplikasi')
data_dari_server_gojek = {
                             'tanggal': '2020-23-11',
                             'driver_list': [
                                 {'nama': 'Eko', 'jarak': 10},
                                 {'nama': 'Dwi', 'jarak': 13},
                                 {'nama': 'Tri', 'jarak': 17},
                                 {'nama': 'Catur', 'jarak': 20}
                             ]
                         },
print(data_dari_server_gojek)
print(f"\nDriver terdekat disekitar sini berjarak {data_dari_server_gojek[0]['driver_list'][0]['jarak']} meter")
# print(f"Driver pertama #1 {data_server_dari_gojek['driver_list'][0]}")
# print(f"Driver pertama #1 {data_server_dari_gojek['driver_list'][2]}")
