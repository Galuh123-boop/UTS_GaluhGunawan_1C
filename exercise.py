# jumlah_siswa = int(input('masukan jumlah siswa : '))
# for x in range(jumlah_siswa):
#     print('masukan nilai siswa ke-{x}')

jumlah_siswa = int(input('masukan jumlah siswa : '))
while x <= 5:
    if x % 2 == 0:
        print(f'{x} - 80')
    else:
        print(f'{x} - 90')
    x += 1
    print('masukan nilai siswa ke-{x}')